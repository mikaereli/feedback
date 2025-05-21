from app.crud.base import BaseCrud
from app.models.purchase import Purchase
from sqlalchemy import select
from app.database import async_session

class PurchaseCrud(BaseCrud):
    model = Purchase
    
    @classmethod
    async def get_user_purchases(cls, user_id: int):
        async with async_session() as session:
            query = (
                select(cls.model).filter_by(user_id=user_id)
            )
            result = await session.execute(query)
            return result.scalars().all()
    
    @classmethod
    async def get_product_purchases(cls, product_id: int):
        async with async_session() as session:
            query = (
                select(cls.model).filter_by(product_id=product_id)
            )
            result = await session.execute(query)
            return result.scalars().all()
