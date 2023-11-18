from typing import Annotated
from pydantic_db_backend_common.pydantic import PaginationParameterModel

from pydantic_db_backend.contexts.pagination_parameter import pagination_parameter_provider

try:
    from fastapi import Body

    async def dep_pagination_parameters(
        skip: Annotated[int | None, Body()] = None,
        limit: Annotated[int | None, Body()] = None,
        sort: Annotated[str | None, Body()] = None,
        view: Annotated[str | None, Body()] = None,
        filter: Annotated[dict | None, Body()] = None,
    ):
        pagination_parameter = PaginationParameterModel(skip=skip, limit=limit, sort=sort, view=view, filter=filter, )
        with pagination_parameter_provider(pagination_parameter):
            yield pagination_parameter

except ImportError:
    pass
