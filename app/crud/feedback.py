from app.crud.base import BaseCrud
from app.models.feedback import Feedback
from app.crud.product import ProductCrud
from sqlalchemy import select, func
from app.database import async_session

class FeedbackCrud(BaseCrud):
    model = Feedback
    
    @classmethod
    async def calculate_and_update_product_rating(cls, product_id: int):
        async with async_session() as session:
            query = select(func.avg(cls.model.rating)).where(cls.model.product_id == product_id)
            result = await session.execute(query)
            avg_rating = result.scalar()

            if avg_rating is None:
                avg_rating = 0
            else:
                avg_rating = round(avg_rating)

            await ProductCrud.update(id=product_id, mean_rating=avg_rating)
            
            return avg_rating
