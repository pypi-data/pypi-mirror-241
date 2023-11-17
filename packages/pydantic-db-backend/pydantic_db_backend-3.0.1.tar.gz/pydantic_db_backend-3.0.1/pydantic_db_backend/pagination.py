from pydantic_db_backend.contexts.pagination_parameter import pagination_parameter_context_var
from pydantic_db_backend_common.pydantic import (
    PaginationResponseModel,
    FindResultModel,
)


def pagination_response(find_result: FindResultModel) -> PaginationResponseModel:
    parameter = pagination_parameter_context_var.get()
    if parameter is None:
        raise ValueError("No pagination_parameter_context set")

    prm = PaginationResponseModel.model_validate(
        parameter.model_dump(exclude_none=True, exclude_unset=True)
    )
    prm.data = {x.uid: x for x in find_result.data}
    prm.max_results = find_result.max_results
    return prm
