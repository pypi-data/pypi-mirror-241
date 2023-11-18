from typing import Type, List, Callable

from pydantic import BaseModel

from pydantic_db_backend.contexts.pagination_parameter import pagination_parameter_context_var
from pydantic_db_backend_common.pydantic import (
    PaginationResponseModel,
    FindResultModel,
    PaginationParameterModel,
)

from pydantic_db_backend.utils import Undefined, resolve_undefined_type_context


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


def pagination_convert_response_list(
    response: PaginationResponseModel,
    model: Type[BaseModel] | None = None,
    callback: Callable[[dict], BaseModel] | None = None,
) -> List[BaseModel]:
    if model is None and callback is None:
        raise ValueError("Either model or callback needs to be defined.")
    if model is not None and callback is not None:
        raise ValueError("Only one parameter can be specified. Either model or callback.")

    if model is not None:
        return [model.model_validate(response.data[uid]) for uid in response.ids]

    if callback is not None:
        return [callback(response.data[uid]) for uid in response.ids]
