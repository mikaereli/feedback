from pydantic import BaseModel

class SFeedback(BaseModel):
    product_id: int
    rating: int
    positive_comment: str
    negative_comment: str
    general_comment: str

    class Config:
        orm_mode = True

class SFeedbackRead(SFeedback):
    user_id: int





