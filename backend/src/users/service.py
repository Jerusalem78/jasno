from sqlalchemy.ext.asyncio import AsyncSession

from core.exceptions import UserNotFoundException
from users.models import UserOrm
from users.repository import UserRepository
from users.schemas import UserRead, UserUpdate


class UserService:
    def __init__(self, session: AsyncSession) -> None:
        self.repository = UserRepository(UserOrm, session)
        self.session = session

    async def get_user(self, user_id: int) -> UserRead:
        user = await self.repository.get_by_id(user_id)
        if user is None:
            raise UserNotFoundException()
        return UserRead.model_validate(user)

    async def get_users(self) -> list[UserRead]:
        users = await self.repository.get_all()
        return [UserRead.model_validate(user) for user in users]

    async def update_user(self, user_id: int, data: UserUpdate) -> UserRead:
        changes = data.model_dump(exclude_unset=True, exclude_none=True)
        if not changes:
            return await self.get_user(user_id)

        user = await self.repository.update(
            user_id,
            **changes,
        )
        if user is None:
            raise UserNotFoundException()

        await self.session.commit()
        return UserRead.model_validate(user)

    async def delete_user(self, user_id: int) -> UserRead:
        user = await self.repository.delete(user_id)
        if user is None:
            raise UserNotFoundException()

        await self.session.commit()
        return UserRead.model_validate(user)
