from core.repository import BaseRepository
from sqlalchemy import select
from core.exceptions import UserAlreadyExistsException

class UserRepository(BaseRepository):

    def __init__(self, model, session):
        super().__init__(model, session)

    async def get_by_email(self, email : str):
        stmt = select(self.model).where(self.model.email == email)
        return await self.session.scalar(stmt)

    async def email_exist(self, email : str):
        user = await self.get_by_email(email=email)
        if user:
            raise UserAlreadyExistsException()

        return True

    