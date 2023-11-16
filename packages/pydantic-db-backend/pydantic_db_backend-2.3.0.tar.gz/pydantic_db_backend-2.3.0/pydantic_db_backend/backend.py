from __future__ import annotations

import hashlib
import json
import logging
import re
from abc import ABC, abstractmethod
from typing import Type, Dict, List, Tuple, Callable

import pydash
from pydantic_settings import BaseSettings

from pydantic_db_backend.utils import CustomJSONEncoder
from pydantic_db_backend_common.exceptions import IndexNotExisting
from pydantic_db_backend_common.indexes import Index
from pydantic_db_backend_common.pydantic import BackendModel, FindResultModel
from pydantic_db_backend_common.utils import uid, utcnow

log = logging.getLogger(__name__)


class Backend(ABC):
    _clients: Dict[str, Backend] = {}
    _collections: Dict[Type[BackendModel], str] = {}
    _revision_ignored_fields: List[str] = ["updated_time"]
    _indexes: Dict[str, list] = {}

    settings_class: Type[BaseSettings] | None = None
    features: List[str] = []

    def __init__(self, alias: str = "default"):
        self.settings = self.settings_class() if self.settings_class is not None else {}
        # noinspection PyTypeChecker
        Backend.set_client(alias, self)

    @classmethod
    def set_client(cls, alias: str, backend: Backend):
        cls._clients[alias] = backend

    @classmethod
    def client(cls, alias: str = "default") -> Backend:
        # todo: raise error if alias not known
        return cls._clients[alias]

    @classmethod
    def collection_name(cls, model: Type[BackendModel]) -> str:
        if model not in cls._collections:
            name = (
                re.sub("([A-Z]+)", r"_\1", model.__name__).lower().removeprefix("_").removesuffix("_model")
            )
            cls._collections[model] = name
        return cls._collections[model]

    @classmethod
    def get_document_revision(cls, document: dict, field: str = "_rev") -> str:
        return pydash.default_to(pydash.get(document, field, None), "0-0")

    @classmethod
    def set_document_revision(cls, document: dict, field: str = "_rev") -> dict:
        old_rev, old_checksum = cls.get_document_revision(document).split("-")
        document_data = pydash.omit(document, field, *cls._revision_ignored_fields)
        checksum = hashlib.md5(
            json.dumps(document_data, cls=CustomJSONEncoder, sort_keys=True).encode("utf8")
        ).hexdigest()
        if checksum != old_checksum:
            revision = f"{str(int(old_rev)+1)}-{checksum}"
            document[field] = revision
        return document

    @classmethod
    def to_db(cls, instance: BackendModel, json_dict: bool | None = True) -> dict:
        instance.updated_time = utcnow()
        return json.loads(instance.model_dump_json()) if json_dict else instance.model_dump()

    @classmethod
    def from_db(
        cls, model: Type[BackendModel], document: dict, json_dict: bool | None = True
    ) -> BackendModel:
        return (
            model.model_validate_json(json.dumps(document)) if json_dict else model.model_validate(document)
        )

    def get_uids(
        self,
        model: Type[BackendModel],
        extend_pipeline: List[dict] | None = None,
    ) -> FindResultModel:
        return self.find(
            model=model,
            fields=["_id"],
            func=lambda x: x["_id"],
        )

    def get_instances(
        self,
        model: Type[BackendModel],
        extend_pipeline: List[dict] | None = None,
    ) -> FindResultModel:
        find = self.find(
            model=model,
            func=lambda x: self.from_db(model, x),
        )
        return find

    def indexes(
        self,
        model: Type[BackendModel],
        create_index_kwargs: dict | None,
        force_index_creation: bool = False,
    ) -> List[Index]:
        col_name = self.collection_name(model)
        if col_name not in self._indexes or force_index_creation:
            indexes = self.create_indexes(model, create_index_kwargs)
            self._indexes[col_name] = indexes
        return self._indexes[col_name]

    def get_index_by_name(self, model: Type[BackendModel], name: str) -> Index:
        col_name = self.collection_name(model)
        if col_name not in self._indexes:
            raise IndexNotExisting(model_name=col_name, name=name)
        model_indexes = self._indexes[col_name]
        index = next(filter(lambda x: x.name == name, model_indexes), None)
        if index is None:
            raise IndexNotExisting(model_name=col_name, name=name)
        return index

    def create_indexes(self, model: Type[BackendModel], create_index_kwargs: dict | None) -> List[Index]:
        if not hasattr(model, "Config"):
            return []

        if not hasattr(model.Config, "backend_indexes"):
            return []

        indexes = model.Config.backend_indexes
        for index in indexes:
            self.create_index(self.collection_name(model), index, **create_index_kwargs)
        return indexes

    def create_index(self, collection_name: str, index: Index, **kwargs):
        log.debug(f"[{collection_name}] Creating {index.type} index {index.name}...")

    @abstractmethod
    def delete_collection(self, model: Type[BackendModel]) -> None:
        # delete index info , for recreating it on next collection usage
        col_name = self.collection_name(model)
        if col_name in self._indexes:
            del self._indexes[col_name]

    @abstractmethod
    def post_instance(self, instance: BackendModel) -> BackendModel:  # pragma: nocover
        pass

    @abstractmethod
    def get_instance(self, model: Type[BackendModel], uid: str) -> BackendModel:  # pragma: nocover
        pass

    @abstractmethod
    def put_instance(self, instance: BackendModel, ignore_revision_conflict: bool = False) -> BackendModel:
        pass

    @abstractmethod
    def delete_uid(self, model: Type[BackendModel], uid: str):
        pass

    @abstractmethod
    def find(
        self,
        model: Type[BackendModel],
        fields: List[str] = None,
        func: Callable = None,
    ) -> FindResultModel:
        pass


def has_backend_features(backend: Backend, features: List[str] | None = None):
    return features is None or all([f in backend.features for f in features])
