from sqlalchemy.orm import Mapped, mapped_column, relationship

from advanced_alchemy.extensions.litestar import SQLAlchemyAsyncConfig, AsyncSessionConfig, SQLAlchemyPlugin
from advanced_alchemy import base

from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
import u_config

sql_config = SQLAlchemyAsyncConfig(
    connection_string=u_config.DATABASE_URL,
    session_config=AsyncSessionConfig(expire_on_commit=False),
    create_all=True
)


class UserTable(base.BigIntAuditBase):
    __tablename__ = "user"
    name: Mapped[str]
    surname: Mapped[str]
    password: Mapped[str]


sql_plugin = SQLAlchemyPlugin(
    config=sql_config
)


# ---------------------------------------------------
class UserRepository(
    SQLAlchemyAsyncRepository[UserTable]
):
    model_type = UserTable
    uniquify = True


class UserService(
    SQLAlchemyAsyncRepositoryService[UserTable, UserRepository]
):
    repository_type = UserRepository
    uniquify = True
