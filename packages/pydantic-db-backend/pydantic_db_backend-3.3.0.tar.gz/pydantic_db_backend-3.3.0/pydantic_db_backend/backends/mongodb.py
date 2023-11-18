from __future__ import annotations

import logging
from typing import Dict, Type, List, Callable, Any, Tuple
from urllib.parse import urlparse

import pydash
from bson import SON
from pydantic_db_backend_common.exceptions import (
    NotFound,
    AlreadyExists,
    RevisionConflict,
)
from pydantic_db_backend_common.pydantic import (
    BackendModel,
    FindResultModel,
    AggregationModel,
    PaginationParameterModel,
)
from pydantic_settings import BaseSettings
from pymongo import MongoClient, collection
from pymongo.errors import DuplicateKeyError

from pydantic_db_backend.backend import Backend
from pydantic_db_backend.contexts.custom_aggregation import custom_aggregation_context_var
from pydantic_db_backend.contexts.pagination_parameter import pagination_parameter_context_var
from pydantic_db_backend.utils import concat_aggregation
from pydantic_db_backend_common.utils import Undefined

log = logging.getLogger(__name__)


class MongoDbBackendSettings(BaseSettings):
    mongodb_uri: str


def transform_sort_str(sort: str) -> List[Tuple[str, int]]:
    ret = []
    for s in sort.split(","):
        ss = s.strip()
        direction = -1 if ss.startswith("-") else 1
        name = ss[1:] if ss.startswith("-") else ss
        ret.append((name, direction))
    return ret


class MongoDbBackend(Backend):
    settings_class = MongoDbBackendSettings
    db_name: str
    connection: MongoClient
    features = Backend.features + ["distinct", "find_extend_pipeline", "pagination"]

    def __init__(self, alias: str = "default"):
        super().__init__(alias)
        self.db_name = urlparse(self.settings.mongodb_uri).path.strip("/")
        self.connection = MongoClient(self.settings.mongodb_uri, tz_aware=True)
        self.db = self.connection[self.db_name]

    @classmethod
    def to_db(cls, instance: BackendModel, json_dict: bool | None = False) -> dict:
        document = super().to_db(instance, json_dict=json_dict)
        document = pydash.omit(
            document | {"_id": document["uid"], "_rev": document["revision"]},
            "uid",
            "revision",
        )

        return document

    @classmethod
    def from_db(
        cls, model: Type[BackendModel], document: dict, json_dict: bool | None = False
    ) -> BackendModel:
        document = pydash.omit(
            document | {"uid": document["_id"], "revision": document["_rev"]},
            "_id",
            "_rev",
        )
        return super().from_db(model, document, json_dict)

    def get_collection(self, model: Type[BackendModel]) -> collection:
        collection_name = self.collection_name(model)
        # cls.indexes(model, dict(db=db))
        return self.db[collection_name]

    def delete_collection(self, model: Type[BackendModel]) -> None:
        col = self.get_collection(model)
        col.drop()
        super().delete_collection(model)

    def post_document(self, model: Type[BackendModel], document: dict) -> Dict:
        col = self.get_collection(model)
        try:
            self.set_document_revision(document, field="_rev")
            col.insert_one(document)
        except DuplicateKeyError as e:
            raise AlreadyExists(uid=document["_id"])
        r = col.find_one({"_id": document["_id"]})
        return r

    def post_instance(self, instance: BackendModel) -> BackendModel:
        document = self.to_db(instance)
        document = self.post_document(instance.__class__, document)
        return self.from_db(instance.__class__, document)

    def get_instance(self, model: Type[BackendModel], uid: str) -> BackendModel:
        col = self.get_collection(model)
        entry = col.find_one({"_id": uid})
        if entry is None:
            raise NotFound(uid)
        return self.from_db(model, entry)

    def put_instance(self, instance: BackendModel, ignore_revision_conflict: bool = False) -> BackendModel:
        # get old revision from doc
        # set new revision in doc

        # update doc with old revision

        # if failed, then there are 2 reasons
        #   a) id does not exist anymore.
        #   b) version does not match.

        col = self.get_collection(instance.__class__)
        document = self.to_db(instance)

        old_rev = self.get_document_revision(document)
        self.set_document_revision(document)  # generate new revision hash
        match = {
            "_id": document["_id"],
        }

        if not ignore_revision_conflict:
            match |= {
                "_rev": old_rev,
            }

        r = col.update_one(
            match,
            {"$set": document},
        )
        # did update succeed ?
        if r.modified_count == 1:
            # everything worked.
            return self.from_db(instance.__class__, document)

        else:
            # update didn't work. try to find document in db.
            r = col.find_one({"_id": document["_id"]})
            if r is not None:
                # document exists , check version
                raise RevisionConflict(r["_rev"])
            else:
                # No document, post
                return self.post_instance(instance)

    def delete_uid(self, model: Type[BackendModel], uid: str) -> None:
        col = self.get_collection(model)
        r = col.delete_one({"_id": uid})  # assuming that there is only one
        if r.deleted_count == 0:
            raise NotFound(uid=uid)

    @staticmethod
    def _convert_query_filter(filter: dict) -> dict:
        # {'worker_expires': {'$and': [{'$ne': None}, {'$lt': '2022-01-01T00:10:00+00:00'}]}}
        def convert(d: Any) -> Any:
            if isinstance(d, dict):
                if len(d) == 1 and list(d.keys())[0] == "$and":
                    return pydash.assign({}, *d["$and"])
            return d

        ret = {k: convert(v) for k, v in filter.items()}
        return ret

    def compile_aggregation(
        self, pagination_parameter: PaginationParameterModel | None | Type[Undefined] = Undefined
    ) -> AggregationModel:
        ret = AggregationModel()

        if pagination_parameter is Undefined:
            pp = pagination_parameter_context_var.get()
        elif pagination_parameter is None:
            pp = PaginationParameterModel()
        else:
            pp = pagination_parameter

        # if pp is None:
        #     raise NotImplementedError

        ext_agg = custom_aggregation_context_var.get()

        skip = None if pp.skip is not None and pp.skip == 0 else pp.skip
        limit = None if pp.limit is not None and pp.limit == 0 else pp.limit
        sort = None if pp.sort is not None and len(pp.sort.strip()) == 0 else pp.sort

        filter = pp.filter  # transform filter

        match = []
        tail = []
        before_tail = None if ext_agg is None else ext_agg.before_tail

        if filter is not None:
            match.append({"$match": filter})

        if sort is not None:
            # transform sorts
            list_sort_tuples = transform_sort_str(sort)
            sort = SON(list_sort_tuples)
            tail.append({"$sort": sort})

        if skip is not None:
            tail.append({"$skip": skip})

        if limit is not None:
            tail.append({"$limit": limit})

        ret.use_facet = not all([sort is None, skip is None, limit is None])

        if ret.use_facet:
            tail = [
                {
                    "$facet": {
                        "meta": [{"$group": {"_id": None, "max_results": {"$sum": 1}}}],
                        "data": tail,
                    }
                }
            ]

        ret.pipeline = concat_aggregation(match, before_tail, tail)
        return ret

    def find(
        self,
        model: Type[BackendModel],
        fields: List[str] = None,
        func: Callable = None,
        pagination_parameter: PaginationParameterModel | None | Type[Undefined] = Undefined,
    ) -> FindResultModel:
        agg = self.compile_aggregation(pagination_parameter)

        try:
            col = self.get_collection(model)
            agg_iterator = col.aggregate(agg.pipeline)

            if agg.use_facet:
                agg_result = next(iter(agg_iterator), None)
                ret = FindResultModel(
                    data=agg_result["data"],
                    max_results=pydash.get(agg_result, ["meta", 0, "max_results"], 0),
                )
            else:
                agg_result = [x for x in agg_iterator]
                ret = FindResultModel(data=agg_result, max_results=len(agg_result))

        except Exception as e:
            raise e

        ret.data = [func(x) for x in ret.data]
        return ret
