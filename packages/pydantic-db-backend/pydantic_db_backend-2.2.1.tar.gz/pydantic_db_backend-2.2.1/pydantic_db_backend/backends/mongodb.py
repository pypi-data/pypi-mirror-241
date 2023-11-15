from __future__ import annotations

import json
import logging
from typing import Dict, Type, List, Tuple, Callable, Any
from urllib.parse import urlparse

import couchdb
import pydash
from bson import SON
from pydantic_db_backend_common.exceptions import (
    NotFound,
    AlreadyExists,
    RevisionConflict,
)
from pydantic_db_backend_common.indexes import AggregationIndex
from pydantic_db_backend_common.pydantic import BackendModel
from pydantic_settings import BaseSettings
from pymongo import MongoClient, collection
from pymongo.errors import DuplicateKeyError

from pydantic_db_backend.backend import Backend
from pydantic_db_backend.utils import CustomJSONEncoder, CustomJSONDecoder

log = logging.getLogger(__name__)


class MongoDbBackendSettings(BaseSettings):
    mongodb_uri: str


class MongoDbBackend(Backend):
    settings_class = MongoDbBackendSettings
    db_name: str
    connection: MongoClient
    features = Backend.features + ["distinct", "find_extend_pipeline"]

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

    def find(
        self,
        model: Type[BackendModel],
        skip: int = 0,
        limit: int = 25,
        query_filter: dict = None,
        sort: List = None,
        fields: List[str] = None,
        max_results: bool | None = False,
        func: Callable = None,
        extend_pipeline: List[dict] | None = None,
    ) -> Tuple[List[Any], int] | List[Any]:
        # fix 0 limit, since couchdb does not know this
        limit = 9999999 if limit == 0 else limit

        if query_filter is None:
            query_filter = {}

        # convert to json and back again, to have real datetime objects
        query_filter = json.loads(json.dumps(query_filter, cls=CustomJSONEncoder), cls=CustomJSONDecoder)
        query_filter = self._convert_query_filter(query_filter)

        col = self.get_collection(model)

        data = []
        if sort is not None and len(sort) != 0:
            sort = SON([(f, 1 if d.lower() == "asc" else -1) for x in sort for f, d in x.items()])
            data.append({"$sort": sort})

        data.append({"$skip": skip})
        data.append({"$limit": limit})

        # if fields is not None:
        #     find_dict |= {"fields": fields}

        agg = [{"$match": query_filter}]
        if extend_pipeline is not None:
            agg.extend(extend_pipeline)
        agg.extend(
            [
                {
                    "$facet": {
                        "meta": [{"$group": {"_id": None, "max_results": {"$sum": 1}}}],
                        "data": data,
                    }
                }
            ]
        )

        try:
            agg_result = next(iter(col.aggregate(agg)), None)

        except Exception as e:
            raise e

        if agg_result is None:
            result = []
            ret_max_results = 0
        else:
            ret_max_results = pydash.get(agg_result, ["meta", 0, "max_results"], 0)
            result = [func(x) for x in pydash.get(agg_result, ["data"], [])]

        if max_results:
            return result, ret_max_results
        else:
            return result
