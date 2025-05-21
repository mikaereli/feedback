from app.crud.base import BaseCrud
from app.models.product import Product
from sqlalchemy import select, insert
from app.database import async_session

class ProductCrud(BaseCrud):
    model = Product
    
    @classmethod
    async def add(cls, **data):
        if 'mean_rating' not in data:
            data['mean_rating'] = 0
            
        async with async_session() as session:
            query = (
                insert(cls.model).values(**data).returning(cls.model)
            )
            result = await session.execute(query)
            await session.commit()
            return result.scalars().first()
