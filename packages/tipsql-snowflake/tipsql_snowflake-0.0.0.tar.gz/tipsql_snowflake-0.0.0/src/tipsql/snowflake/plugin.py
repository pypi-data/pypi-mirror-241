from typing import Literal, override

from tipsql.core.dataclasses import extra_forbid_dataclass
from tipsql.core.plugins.database_plugin import TipsqlDatabasePlugin


@extra_forbid_dataclass
class SnowflakeDatabaseConfig:
    type: Literal["snowflake"]


class SnowflakeDatabasePlugin(TipsqlDatabasePlugin):
    @property
    def database_name(self) -> str:
        return "snowflake"

    @property
    def database_config(self) -> type[SnowflakeDatabaseConfig]:
        return SnowflakeDatabaseConfig

    @override
    def sync_database(self, config: SnowflakeDatabaseConfig) -> None:
        print("syncing snowflake database")

        return None
