import sqlite3

from tipsql.sqlite3.cursor import Cursor


class Connection:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self._connection = connection

    def close(self) -> None:
        self._connection.close()

    def commit(self) -> None:
        self._connection.commit()

    def rollback(self) -> None:
        self._connection.rollback()

    def cursor(self) -> Cursor:
        return Cursor(self._connection.cursor())
