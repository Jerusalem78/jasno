from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from core.settings import setting, debug
from typing import Annotated
from sqlalchemy import func, DateTime
from sqlalchemy.orm import mapped_column, Mapped
import datetime

engine = create_async_engine(
    setting.DATABASE_URL,
    echo=debug,
)

async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit= False,
)

intpk = Annotated[
    int,
    mapped_column(primary_key=True),
]

created_at_type = Annotated[
    datetime.datetime,
    mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    ),
]

updated_at_type = Annotated[
    datetime.datetime,
    mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    ),
]
class Base(DeclarativeBase):
    pass

async def get_db() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
