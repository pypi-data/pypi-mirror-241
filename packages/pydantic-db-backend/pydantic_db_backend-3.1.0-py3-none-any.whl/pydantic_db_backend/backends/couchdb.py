###
### DEPRECATED ATM. Focus is on mongdb backend until feature completeness
###

from __future__ import annotations

import json
import logging
import os
from typing import Dict, Type, List, Tuple, Callable, Any

import couchdb
import pydash
from couchdb import ResourceConflict, ServerError
from pydantic import BaseModel, Field
from pydantic_db_backend_common.exceptions import (
    NotFound,
    AlreadyExists,
    RevisionConflict,
)
from pydantic_db_backend_common.indexes import Index, SortingIndex, AggregationIndex
from pydantic_db_backend_common.pydantic import BackendModel, FindResultModel
from pydantic_settings import BaseSettings

from pydantic_db_backend.backend import Backend
from pydantic_db_backend.utils import CustomJSONEncoder

log = logging.getLogger(__name__)


class CouchDbBackendSettings(BaseSettings):
    couchdb_uri: str


class CouchDbBackend(Backend):
    settings_class = CouchDbBackendSettings
    connection: CouchDbConnectionModel
    features = Backend.features

    def __init__(self, alias: str = "default"):
        super().__init__(alias)
        uri = self.settings.couchdb_uri
        self.connection = CouchDbConnectionModel(alias=alias, uri=uri, server=couchdb.Server(uri))

    @classmethod
    def to_db(cls, instance: BackendModel, json_dict: bool | None = True) -> dict:
        document = super().to_db(instance)
        document = pydash.omit(
            document | {"_id": document["uid"], "_rev": document["revision"]},
            "uid",
            "revision",
        )
        return document

    @classmethod
    def from_db(
        cls, model: Type[BackendModel], document: dict, json_dict: bool | None = True
    ) -> BackendModel:
        document = pydash.omit(
            document | {"uid": document["_id"], "revision": document["_rev"]},
            "_id",
            "_rev",
        )
        return super().from_db(model, document)

    def get_collection(self, model: Type[BackendModel]) -> couchdb.Database:
        collection_name = self.collection_name(model)
        con = self.connection

        if collection_name in con.server:
            col = con.server[collection_name]
        else:
            col = con.server.create(collection_name)
            self.indexes(model, dict(collection=col))
        return col

    def delete_collection(self, model: Type[BackendModel]) -> None:
        server = self.connection.server
        name = self.collection_name(model)
        if name in server:
            server.delete(name)
        super().delete_collection(model)

    def post_document(self, model: Type[BackendModel], document: dict) -> Dict:
        col = self.get_collection(model)
        try:
            col.save(pydash.omit(document, "_rev"))
        except ResourceConflict as e:
            raise AlreadyExists(uid=document["_id"])
        return col.get(document["_id"])

    def post_instance(self, instance: BackendModel) -> BackendModel:
        document = self.to_db(instance)
        document = self.post_document(instance.__class__, document)
        return self.from_db(instance.__class__, document)

    def get_instance(self, model: Type[BackendModel], uid: str) -> BackendModel:
        col = self.get_collection(model)
        entry = col.get(uid)
        if entry is None:
            raise NotFound(uid)
        return self.from_db(model, entry)

    def put_instance(self, instance: BackendModel, ignore_revision_conflict: bool = False) -> BackendModel:
        col = self.get_collection(instance.__class__)
        if instance.uid in col:
            document = self.to_db(instance)
            while True:
                try:
                    id, rev = col.save(document)
                    document["_rev"] = rev
                    return self.from_db(instance.__class__, document)

                except ResourceConflict as e:
                    new_rev = col.get(instance.uid)["_rev"]
                    if ignore_revision_conflict:
                        document["_rev"] = new_rev
                        continue
                    raise RevisionConflict(new_rev)

        else:
            return self.post_instance(instance)

    def delete_uid(cls, model: Type[BackendModel], uid: str) -> None:
        col = cls.get_collection(model)
        if uid in col:
            del col[uid]
        else:
            raise NotFound(uid=uid)

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
    ) -> FindResultModel:
        # fix 0 limit, since couchdb does not know this
        limit = 9999999 if limit == 0 else limit

        if query_filter is None:
            query_filter = {}

        # convert to json and back again, to have iso datetime strings
        query_filter = json.loads(json.dumps(query_filter, cls=CustomJSONEncoder))

        col = self.get_collection(model)

        find_dict = {
            "selector": query_filter,
            "skip": skip,
            "limit": limit,
        }

        if fields is not None:
            find_dict |= {"fields": fields}

        if sort is not None:
            find_dict["sort"] = sort

        try:
            find_result = col.find(find_dict)
        except ServerError as e:
            error_code = pydash.get(e, ["args", 0, 0])

            if error_code == 400:
                # @asc:  not what I expected the system to do. Better would be to modify the
                # index cache and initiate a new get_db... and a loop
                self.indexes(model, dict(collection=col), force_index_creation=True)
                find_result = col.find(find_dict)
            else:
                raise e

        return FindResultModel(
            data=[func(x) for x in find_result],
            max_results=0 if not max_results else self.get_max_results(model, query_filter),
        )

    def get_max_results(self, model: Type[BackendModel], query_filter: dict) -> int:
        # atm it only works with one field,
        col = self.get_collection(model)

        field = "_".join(list(query_filter.keys()))
        view_name = f"{field}_sum"
        index = self.get_index_by_name(model, view_name)

        design_document = f"aggregation_{view_name}/{view_name}"
        for row in col.view(design_document, group=True):
            if field == "":
                return row.value
            else:
                for k, v in query_filter.items():
                    if isinstance(v, dict):
                        k = next(iter(v.keys()))
                        if k == "$eq":
                            v = v[k]
                        else:
                            return 0
                    if v == row.key:
                        ret = row.value
                        return ret

    # noinspection PyMethodOverriding
    def create_index(self, collection_name: str, index: Index, collection: couchdb.Database):
        super().create_index(collection_name, index)

        if index.type == "sorting":
            index: SortingIndex

            index_key = (collection_name, index.name)
            indexes = collection.index()

            # noinspection PyUnboundLocalVariable
            if index_key not in indexes:
                indexes[index_key] = index.sorting

        elif index.type == "aggregation":
            index: AggregationIndex
            self.view_from_aggregation_index(collection, index)

        else:
            pass

    def view_from_aggregation_index(self, collection: couchdb.Database, index: AggregationIndex):
        design_document = index.design_document

        in_db = f"_design/{design_document}" in collection
        if not in_db:
            field, func = next(iter(index.spec.items()))
            if field is None or field == "":
                map_function = f"function (doc) {{ emit(null, 1); }}"
            else:
                map_function = f"function (doc) {{ emit(doc.{field}, 1); }}"
            view_name = f"{index.view_name}"
            # reduce_function = f"function(keys, values, rereduce) {{ return sum(values); }}"
            data = {
                "_id": f"_design/{design_document}",
                "views": {view_name: {"map": map_function, "reduce": func}},
                "language": "javascript",
                "options": {"partitioned": False},
            }
            logging.info(f"creating view {design_document}/{view_name}")
            collection.save(data)


class CouchDbConnectionModel(BaseModel):
    alias: str
    uri: str
    server: couchdb.Server
    dbs: Dict[str, couchdb.Database] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True
