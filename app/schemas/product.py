from pydantic import BaseModel, ConfigDict
from typing import Optional

class SProductCreate(BaseModel):
    cost: int
    amount: int
    description: str

class SProduct(BaseModel):
    id: int
    cost: int
    amount: int
    description: str
    mean_rating: Optional[int] = 0

    model_config = ConfigDict(from_attributes=True)
