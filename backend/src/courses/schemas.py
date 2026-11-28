from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from core.enums import LangEnum, LevelEnum

class CourseBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1)
    language: LangEnum
    level: LevelEnum


class CourseCreate(CourseBase):
    is_published: bool = False


class CourseUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = Field(default=None, min_length=1)
    language: LangEnum | None = None
    level: LevelEnum | None = None
    is_published: bool | None = None


class CourseRead(CourseBase):
    id: int
    is_published: bool
    created_by_id: int | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
