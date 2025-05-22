from pydantic import BaseModel, conint

class SFeedback(BaseModel):
    product_id: int
    rating: conint(ge=1, le=5)
    positive_comment: str
    negative_comment: str
    general_comment: str

    class Config:
        orm_mode = True

class SFeedbackRead(SFeedback):
    user_id: int





