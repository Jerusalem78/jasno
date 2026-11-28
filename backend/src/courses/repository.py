from core.repository import BaseRepository
from courses.models import CourseOrm


class CourseRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(CourseOrm, session)
