import contextlib
from contextvars import ContextVar

from pydantic_db_backend_common.pydantic import PaginationParameterModel

pagination_parameter_context_var: ContextVar[PaginationParameterModel | None] = ContextVar(
    "pagination_parameter_context_var", default=None
)


@contextlib.contextmanager
def pagination_parameter_provider(parameter: PaginationParameterModel):
    token = pagination_parameter_context_var.set(parameter)
    yield parameter
    pagination_parameter_context_var.reset(token)


@contextlib.contextmanager
def pagination_parameter_context():
    yield pagination_parameter_context_var.get()
