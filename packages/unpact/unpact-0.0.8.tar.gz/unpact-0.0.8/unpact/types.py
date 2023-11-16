from typing import Any, Callable, Protocol, Tuple, TypedDict, Union, runtime_checkable
import sys

if sys.version_info < (3, 12):
    from typing_extensions import TypedDict  # noqa: F811
else:
    from typing import TypedDict

__all__ = ["ColumnDef", "ColumnFormatter", "ColumnSpec"]


@runtime_checkable
class IndexFormatter(Protocol):
    def __call__(self, data: Any, index: int = ...):
        ...  # pragma: no cover


ColumnFormatter = Union[IndexFormatter, Callable[[Any], Any]]


class ColumnSpec(TypedDict, total=False):
    name: str
    formatter: ColumnFormatter


ColumnDef = Union[Tuple[str, ColumnSpec], str]
