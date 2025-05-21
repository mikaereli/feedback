from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    rating = Column(Integer)
    positive_comment = Column(String)
    negative_comment = Column(String)
    general_comment = Column(String)
