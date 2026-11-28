from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from courses.schemas import CourseCreate, CourseRead, CourseUpdate
from courses.service import CourseService


course_router = APIRouter(prefix="/courses", tags=["courses"])


def get_course_service(session: AsyncSession = Depends(get_db)) -> CourseService:
    return CourseService(session)


@course_router.get("", response_model=list[CourseRead])
async def get_courses(service: CourseService = Depends(get_course_service)) -> list[CourseRead]:
    return await service.get_courses()


@course_router.get("/{course_id}", response_model=CourseRead)
async def get_course(
    course_id: int,
    service: CourseService = Depends(get_course_service),
) -> CourseRead:
    return await service.get_course(course_id)


@course_router.post("", response_model=CourseRead)
async def create_course(
    user_id: int,
    data: CourseCreate,
    service: CourseService = Depends(get_course_service),
) -> CourseRead:
    return await service.create_course(data, user_id)


@course_router.patch("/{course_id}", response_model=CourseRead)
async def update_course(
    course_id: int,
    user_id: int,
    data: CourseUpdate,
    service: CourseService = Depends(get_course_service),
) -> CourseRead:
    return await service.update_course(course_id, data, user_id)


@course_router.delete("/{course_id}", response_model=CourseRead)
async def delete_course(
    course_id: int,
    user_id: int,
    service: CourseService = Depends(get_course_service),
) -> CourseRead:
    return await service.delete_course(course_id, user_id)
