from sqlalchemy import Column, Integer, String

from app.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    cost = Column(Integer)
    amount = Column(Integer)
    description = Column(String)
    mean_rating = Column(Integer, default=0)
