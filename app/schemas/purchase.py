from pydantic import BaseModel, ConfigDict
from datetime import datetime

class SPurchaseCreate(BaseModel):
    product_id: int
    quantity: int = 1

class SPurchase(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    purchase_date: datetime

    model_config = ConfigDict(from_attributes=True)
