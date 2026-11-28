from core.database import Base, intpk, created_at_type, updated_at_type
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey
from core.enums import LangEnum, UserRole
from datetime import datetime

class UserOrm(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    email : Mapped[str] = mapped_column(unique=True)
    password_hash : Mapped[str]
    name : Mapped[str]
    role : Mapped[UserRole]
    native_language : Mapped[LangEnum] = mapped_column(default=LangEnum.RU)
    learning_language : Mapped[LangEnum] = mapped_column(default=LangEnum.EN)
    daily_goal_minutes : Mapped[int] = mapped_column(default=15)
    is_active : Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[created_at_type]
    updated_at: Mapped[updated_at_type]
    email_verified_at : Mapped[datetime | None]

    def __str__(self) -> str:
        return str(self.id)

class UserCourseOrm(Base):
    __tablename__ = "user_courses"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id", ondelete="CASCADE"), primary_key=True)
