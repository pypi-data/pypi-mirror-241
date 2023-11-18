""" SQLite3 data types.

See: https://www.sqlite.org/datatype3.html
"""

import datetime

from tipsql.core.operator.eq_operator import EqOperator
from tipsql.core.operator.not_eq_operator import NotEqOperator
from tipsql.core.relation.column import ColumnType


class Bool(ColumnType[bool]):
    """SQLite does not have a separate Boolean storage class.

    Instead, Boolean values are stored as integers 0 (false) and 1 (true).
    """

    __slots__ = ()


class Integer(
    ColumnType[int],
    EqOperator[int, int],
    NotEqOperator[int, int],
):
    __slots__ = ()


class Real(
    ColumnType[float],
    EqOperator[float, float | int],
    NotEqOperator[float, float | int],
):
    __slots__ = ()


class Text(
    ColumnType[str],
    EqOperator[str, str],
    NotEqOperator[str, str],
):
    __slots__ = ()


class Blob(ColumnType[bytes]):
    __slots__ = ()


class DateTime[T: Text | Real | Integer](
    ColumnType[datetime.datetime],
    EqOperator[datetime.datetime, datetime.datetime],
    NotEqOperator[datetime.datetime, datetime.datetime],
):
    """SQLite does not have a storage class set aside for storing dates and/or times.

    Instead, the built-in Date And Time Functions of SQLite
    are capable of storing dates and times as TEXT, REAL, or INTEGER values.
    """

    __slots__ = "_sql_type"

    def __init__(
        self,
        sql_type: T,
        schema_name: str | None,
        table_name: str,
        column_name: str,
        py_type: type,
    ) -> None:
        self._sql_type = sql_type
        super().__init__(
            schema_name,
            table_name,
            column_name,
            py_type,
        )


class Date[T: Text | Real | Integer](
    ColumnType[datetime.date],
    EqOperator[datetime.date, datetime.date],
    NotEqOperator[datetime.date, datetime.date],
):
    """SQLite does not have a storage class set aside for storing dates.

    Instead, the built-in Date And Time Functions of SQLite
    are capable of storing dates as TEXT, REAL, or INTEGER values.
    """

    __slots__ = "_sql_type"

    def __init__(
        self,
        sql_type: T,
        schema_name: str | None,
        table_name: str,
        column_name: str,
        py_type: type,
    ) -> None:
        self._sql_type = sql_type
        super().__init__(
            schema_name,
            table_name,
            column_name,
            py_type,
        )


class Time[T: Text | Real | Integer](
    ColumnType[datetime.time],
    EqOperator[datetime.time, datetime.time],
    NotEqOperator[datetime.time, datetime.time],
):
    """SQLite does not have a storage class set aside for storing dates.

    Instead, the built-in Date And Time Functions of SQLite
    are capable of storing dates as TEXT, REAL, or INTEGER values.
    """

    __slots__ = "_sql_type"

    def __init__(
        self,
        sql_type: T,
        schema_name: str | None,
        table_name: str,
        column_name: str,
        py_type: type,
    ) -> None:
        self._sql_type = sql_type
        super().__init__(
            schema_name,
            table_name,
            column_name,
            py_type,
        )
