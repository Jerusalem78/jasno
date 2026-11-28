from core.database import Base, intpk, updated_at_type,created_at_type
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from core.enums import LangEnum, LevelEnum

class CourseOrm(Base):

    __tablename__ = 'courses'

    id :  Mapped[intpk]
    title : Mapped[str] 
    description : Mapped[str]
    language : Mapped[LangEnum]
    level : Mapped[LevelEnum]
    is_published : Mapped[bool]
    created_by_id: Mapped[int | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at : Mapped[created_at_type]
    updated_at : Mapped[updated_at_type]

    
