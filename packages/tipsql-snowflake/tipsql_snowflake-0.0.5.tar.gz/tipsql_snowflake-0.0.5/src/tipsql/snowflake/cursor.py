from logging import getLogger
from typing import Any, Sequence, overload

from tipsql.core.query.builder import BuildProtcol

from snowflake.connector.cursor import ResultMetadata, SnowflakeCursor

logger = getLogger(__name__)


class Cursor:
    def __init__(self, cursor: SnowflakeCursor) -> None:
        self._cursor = cursor

    @property
    def description(self) -> list[ResultMetadata]:
        return self._cursor.description

    @property
    def rowcount(self) -> int | None:
        return self._cursor.rowcount

    @overload
    def callproc(self, procname: str) -> tuple:
        ...

    @overload
    def callproc[T: Sequence](self, procname: str, args: T) -> T:
        ...

    def callproc[T: Sequence](self, procname: str, args: T = tuple()) -> T | tuple:
        return self._cursor.callproc(procname, *args)

    def close(self) -> bool | None:
        return self._cursor.close()

    @overload
    def execute(
        self, operation: BuildProtcol, parameters: None = None
    ) -> SnowflakeCursor | None:
        ...

    @overload
    def execute(
        self, operation: str, parameters: Sequence[Any] | dict[Any, Any] | None = None
    ) -> SnowflakeCursor | None:
        ...

    def execute(
        self,
        operation: BuildProtcol | str,
        parameters: Sequence[Any] | dict[Any, Any] | None = None,
    ):
        if isinstance(operation, str):
            pass
        else:
            operation, parameters = operation.build(
                {"style": "pyformat", "stringify": True}
            )

        logger.debug(f'query: "{operation}"')
        logger.debug(f"params: {parameters}")

        return self._cursor.execute(operation, parameters)
