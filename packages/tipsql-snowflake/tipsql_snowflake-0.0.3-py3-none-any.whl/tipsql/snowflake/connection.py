import os
from typing import Self

from tipsql.snowflake.cursor import Cursor

from snowflake.connector import SnowflakeConnection, connect


class Connection:
    def __init__(self, connection: SnowflakeConnection) -> None:
        self._connection = connection

    @classmethod
    def from_env(cls) -> Self:
        return cls(
            connect(
                user=os.environ["SNOWFLAKE_USER"],
                password=os.environ["SNOWFLAKE_PASSWORD"],
                account=os.environ["SNOWFLAKE_ACCOUNT"],
                database=os.environ["SNOWFLAKE_DATABASE"],
                schema=os.environ["SNOWFLAKE_SCHEMA"],
                warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
                role=os.environ["SNOWFLAKE_ROLE"],
            )
        )

    def close(self) -> None:
        self._connection.close()

    def commit(self) -> None:
        self._connection.commit()

    def rollback(self) -> None:
        self._connection.rollback()

    def cursor(self) -> Cursor:
        return Cursor(self._connection.cursor())
