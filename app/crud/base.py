from sqlalchemy import select, insert, update
from app.database import async_session


class BaseCrud:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
            async with async_session() as session:
                query = select(cls.model.__table__.columns).filter_by(**filter_by)
                result = await session.execute(query)
                return result.mappings().one_or_none()
    
    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session() as session:
            query = (
                select(cls.model).filter_by(**filter_by)
            )
            result = await session.execute(query)
            return result.scalars().all()
    
    @classmethod
    async def add(cls, **data):
        async with async_session() as session:
            query = (
                insert(cls.model).values(**data).returning(cls.model)
            )
            result = await session.execute(query)
            await session.commit()
            return result.scalars().first()  # Return the created object

    @classmethod
    async def update(cls, id: int, **data):
        async with async_session() as session:
            query = (
                update(cls.model)
                .where(cls.model.id == id)
                .values(**data)
                .returning(cls.model)
            )
            result = await session.execute(query)
            await session.commit()
            return result.scalars().first()

    @classmethod
    async def delete(cls, **filter_by):
        async with async_session() as session:
            query = (
                cls.model.delete().filter_by(**filter_by)
            )
            await session.execute(query)
            await session.commit()