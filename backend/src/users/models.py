from core.database import Base, intpk, created_at_type, updated_at_type
from sqlalchemy.orm import mapped_column, Mapped
from core.enums import LangEnum, LevelEnum
from datetime import datetime

class UserOrm(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    email : Mapped[str] = mapped_column(unique=True)
    password_hash : Mapped[str]
    name : Mapped[str]
    native_language : Mapped[LangEnum] = mapped_column(default=LangEnum.RU)
    learning_language : Mapped[LangEnum] = mapped_column(default=LangEnum.EN)
    daily_goal_minutes : Mapped[int] = mapped_column(default=15)
    is_active : Mapped[bool] = mapped_column(default=True)
    language_level : Mapped[LevelEnum] = mapped_column(default=LevelEnum.A1)
    created_at: Mapped[created_at_type]
    updated_at: Mapped[updated_at_type]
    email_verified_at : Mapped[datetime | None]

    def __str__(self) -> str:
        return str(self.id)
