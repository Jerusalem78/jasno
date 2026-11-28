from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

class BaseRepository:

    def __init__(self, model, session : AsyncSession):
        self.model = model
        self.session = session

    async def get_all(self):
        stmt = select(self.model)
        result = await self.session.scalars(stmt)
        return list(result.all())

    async def get_by_id(self, id : int):
        stmt = select(self.model).where(self.model.id == id)
        return await self.session.scalar(stmt)

    async def create(self, **data):
        stmt = insert(self.model).values(**data).returning(self.model)
        result = await self.session.scalars(stmt)
        return result.first()

    async def delete(self, id : int):
        stmt = (
            delete(self.model)
            .where(self.model.id == id)
            .returning(self.model)
        )
        result = await self.session.scalars(stmt)
        return result.first()

    async def update(self, id: int, **data):
        if not data:
            return await self.select_by_id(id)

        stmt = (
            update(self.model)
            .where(self.model.id == id)
            .values(**data)
            .returning(self.model)
        )
        result = await self.session.scalars(stmt)
        return result.first()
