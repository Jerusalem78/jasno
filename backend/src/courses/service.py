from sqlalchemy.ext.asyncio import AsyncSession

from core.enums import UserRole
from core.exceptions import CourseNotFoundException, CoursePermissionException, UserNotFoundException
from users.models import UserOrm
from courses.repository import CourseRepository
from courses.schemas import CourseCreate, CourseRead, CourseUpdate


class CourseService:
    def __init__(self, session: AsyncSession) -> None:
        self.repository = CourseRepository(session)
        self.session = session

    async def get_course(self, course_id: int) -> CourseRead:
        course = await self.repository.get_by_id(course_id)
        if course is None:
            raise CourseNotFoundException()
        return CourseRead.model_validate(course)

    async def get_courses(self) -> list[CourseRead]:
        courses = await self.repository.get_all()
        return [CourseRead.model_validate(course) for course in courses]

    async def create_course(self, data: CourseCreate, user_id: int) -> CourseRead:
        await self._get_user(user_id)

        course = await self.repository.create(
            **data.model_dump(),
            created_by_id=user_id,
        )
        await self.session.commit()
        return CourseRead.model_validate(course)

    async def update_course(self, course_id: int, data: CourseUpdate, user_id: int) -> CourseRead:
        course = await self.repository.get_by_id(course_id)
        if course is None:
            raise CourseNotFoundException()
        current_user = await self._get_user(user_id)
        self._check_course_permission(course, current_user)

        changes = data.model_dump(exclude_unset=True, exclude_none=True)
        if not changes:
            return CourseRead.model_validate(course)

        course = await self.repository.update(course_id, **changes)
        if course is None:
            raise CourseNotFoundException()

        await self.session.commit()
        return CourseRead.model_validate(course)

    async def delete_course(self, course_id: int, user_id: int) -> CourseRead:
        course = await self.repository.get_by_id(course_id)
        if course is None:
            raise CourseNotFoundException()
        current_user = await self._get_user(user_id)
        self._check_course_permission(course, current_user)

        course = await self.repository.delete(course_id)
        if course is None:
            raise CourseNotFoundException()

        await self.session.commit()
        return CourseRead.model_validate(course)

    @staticmethod
    def _check_course_permission(course, current_user: UserOrm) -> None:
        if current_user.role != UserRole.ADMIN and course.created_by_id != current_user.id:
            raise CoursePermissionException()

    async def _get_user(self, user_id: int) -> UserOrm:
        user = await self.session.get(UserOrm, user_id)
        if user is None:
            raise UserNotFoundException()
        return user
