from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from core.enums import LangEnum, LevelEnum


class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(min_length=1, max_length=100)
    native_language: LangEnum = LangEnum.RU
    learning_language: LangEnum = LangEnum.EN
    daily_goal_minutes: int = Field(default=15, ge=1, le=1440)
    language_level: LevelEnum = LevelEnum.A1


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)


class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    native_language: LangEnum | None = None
    learning_language: LangEnum | None = None
    daily_goal_minutes: int | None = Field(default=None, ge=1, le=1440)
    language_level: LevelEnum | None = None


class UserRead(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    email_verified_at: datetime | None

    model_config = ConfigDict(from_attributes=True)
