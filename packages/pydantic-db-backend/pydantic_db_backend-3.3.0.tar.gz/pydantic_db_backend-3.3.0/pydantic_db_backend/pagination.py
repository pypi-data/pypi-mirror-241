from typing import Type

from pydantic_db_backend.contexts.pagination_parameter import pagination_parameter_context_var
from pydantic_db_backend_common.pydantic import (
    PaginationResponseModel,
    FindResultModel,
    PaginationParameterModel,
)

from pydantic_db_backend_common.utils import resolve_undefined_type_context, Undefined


def pagination_response(
    find_result: FindResultModel,
    pagination_parameter: PaginationParameterModel | None | Type[Undefined] = Undefined,
) -> PaginationResponseModel:
    pagination_parameter = pagination_parameter_resolve(pagination_parameter)

    prm = PaginationResponseModel.model_validate(
        pagination_parameter.model_dump(exclude_none=True, exclude_unset=True)
    )
    prm.data = {x.uid: x for x in find_result.data}
    prm.ids = [x.uid for x in find_result.data]
    prm.max_results = find_result.max_results

    return prm


def pagination_parameter_resolve(
    pagination_parameter: PaginationParameterModel | None | Type[Undefined] = Undefined,
) -> PaginationParameterModel:
    pagination_parameter: PaginationParameterModel = resolve_undefined_type_context(
        pagination_parameter_context_var, PaginationParameterModel, pagination_parameter
    )
    return pagination_parameter.model_copy()
