from typing import Literal, override

from tipsql.core.dataclasses import extra_forbid_dataclass
from tipsql.core.plugins.database_plugin import TipsqlDatabasePlugin


@extra_forbid_dataclass
class Sqlite3DatabaseConfig:
    type: Literal["sqlite3"]


class Sqlite3DatabasePlugin(TipsqlDatabasePlugin):
    @property
    def database_name(self) -> str:
        return "sqlite3"

    @property
    def database_config(self) -> type[Sqlite3DatabaseConfig]:
        return Sqlite3DatabaseConfig

    @override
    def sync_database(self, config: Sqlite3DatabaseConfig) -> None:
        print("syncing sqlite3 database")

        return None
