import contextlib
from contextvars import ContextVar

from pydantic_db_backend_common.pydantic import CustomAggregationModel

custom_aggregation_context_var: ContextVar[CustomAggregationModel | None] = ContextVar(
    "custom_aggregation_context_var", default=None
)


@contextlib.contextmanager
def custom_aggregation_provider(custom_aggregation: CustomAggregationModel):
    token = custom_aggregation_context_var.set(custom_aggregation)
    yield custom_aggregation
    custom_aggregation_context_var.reset(token)
