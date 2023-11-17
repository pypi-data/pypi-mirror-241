from typing import Type

from pydantic_db_backend.contexts.pagination_parameter import pagination_parameter_context_var
from pydantic_db_backend_common.pydantic import (
    PaginationResponseModel,
    FindResultModel,
    PaginationParameterModel,
)

from pydantic_db_backend.utils import Undefined


def pagination_response(
    find_result: FindResultModel,
    pagination_parameter: PaginationParameterModel | None | Type[Undefined] = Undefined,
) -> PaginationResponseModel:
    if pagination_parameter is Undefined:
        pagination_parameter = pagination_parameter_context_var.get()
    elif pagination_parameter is None:
        pagination_parameter = PaginationParameterModel()

    prm = PaginationResponseModel.model_validate(
        pagination_parameter.model_dump(exclude_none=True, exclude_unset=True)
    )
    prm.data = {x.uid: x for x in find_result.data}
    prm.max_results = find_result.max_results
    return prm
