from fastapi import APIRouter, Depends
from users.service import UserService
from users.schemas import UserRead, UserUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db

user_router = APIRouter(prefix='/users',tags=["users"])

def get_user_service(session: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(session)

@user_router.get('/me', response_model=UserRead)
async def get_my_profile(
    # user = Depends(get_current_user),
    user: int,
    service : UserService = Depends(get_user_service)
    ) -> UserRead:
    return await service.get_user(user_id=user)

@user_router.patch('/me', response_model=UserRead)
async def patch_my_profile(
    # user = Depends(get_current_user),
    user: int,
    data: UserUpdate,
    service : UserService = Depends(get_user_service)
    ) -> UserRead:
    return await service.update_user(user_id=user, data=data)

@user_router.delete('/me')
async def delete_my_profile(user : int, service : UserService = Depends(get_user_service)):
    return await service.delete_user(user_id=user)