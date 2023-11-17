from typing import Annotated
from pydantic_db_backend_common.pydantic import PaginationParameterModel

try:
    from fastapi import Body

    async def dep_pagination_parameters(
        skip: Annotated[int | None, Body()] = None,
        limit: Annotated[int | None, Body()] = None,
        sort: Annotated[str | None, Body()] = None,
        view: Annotated[str | None, Body()] = None,
        filter: Annotated[dict | None, Body()] = None,
    ):
        return PaginationParameterModel(
            skip=skip,
            limit=limit,
            sort=sort,
            view=view,
            filter=filter,
        )

except ImportError:
    pass
