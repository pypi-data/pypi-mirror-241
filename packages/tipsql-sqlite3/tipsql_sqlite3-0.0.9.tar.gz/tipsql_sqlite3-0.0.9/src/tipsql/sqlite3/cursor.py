import sqlite3
from logging import getLogger
from typing import Any, Sequence, overload

from tipsql.core.query.builder import BuildProtcol
from tipsql.core.query.statement.insert import InsertQuery

logger = getLogger(__name__)


class Cursor:
    def __init__(self, cursor: sqlite3.Cursor) -> None:
        self._cursor = cursor

    @property
    def description(
        self,
    ) -> tuple[tuple[str, None, None, None, None, None, None], ...] | Any:
        return self._cursor.description

    @property
    def rowcount(self) -> int:
        return self._cursor.rowcount

    def close(self) -> bool | None:
        return self._cursor.close()

    @overload
    def execute(
        self, operation: BuildProtcol, parameters: None = None
    ) -> sqlite3.Cursor:
        ...

    @overload
    def execute(
        self, operation: str, parameters: Sequence[Any] | dict[Any, Any] | None = None
    ) -> sqlite3.Cursor:
        ...

    def execute(
        self,
        operation: BuildProtcol | str,
        parameters: Sequence[Any] | dict[Any, Any] | None = None,
    ):
        if isinstance(operation, str):
            parameters = parameters or ()
        else:
            operation, parameters = operation.build({"style": "qmark"})

        logger.debug(f'query: "{operation}"')
        logger.debug(f"params: {parameters}")

        return self._cursor.execute(operation, parameters)

    @overload
    def execute_many(
        self,
        operation: InsertQuery,
        parameters: None = None,
    ) -> sqlite3.Cursor:
        ...

    @overload
    def execute_many(
        self,
        operation: str,
        parameters: Sequence[Sequence[Any]] | Sequence[dict[Any, Any]] | None = None,
    ) -> sqlite3.Cursor:
        ...

    def execute_many(
        self,
        operation: InsertQuery | str,
        parameters: Sequence[Sequence[Any]] | Sequence[dict[Any, Any]] | None = None,
    ):
        if isinstance(operation, str):
            parameters = parameters or ()
        else:
            operation, parameters = operation.build_many({"style": "qmark"})

        logger.debug(f'query: "{operation}"')
        logger.debug(f"params: {parameters}")

        return self._cursor.executemany(operation, parameters)
