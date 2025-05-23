from typing import List
from fastapi import APIRouter, Depends, Path, HTTPException, status, Form


from app.auth.dependecies import get_current_user
from app.crud.feedback import FeedbackCrud
from app.schemas.feedback import SFeedback, SFeedbackRead
from app.models.user import User


router = APIRouter(prefix="/feedback", tags=["Feedback"])

@router.post("/", response_model=SFeedback)
async def add_feedback(feedback_data: SFeedback = Form(...), user: User = Depends(get_current_user)):
    if not feedback_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Feedback data is required")

    if feedback_data.rating > 5 or feedback_data.rating < 1:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Rating must be between 1 and 5")
    
    feedback_dict = feedback_data.model_dump()
    feedback = await FeedbackCrud.add(user_id=user.id, **feedback_dict)
    await FeedbackCrud.calculate_and_update_product_rating(feedback_dict["product_id"])
    
    return feedback

@router.get("/by_product/{product_id}", response_model=List[SFeedbackRead])
async def get_feedbacks_by_product(product_id: int = Path(..., gt=0)):
    return await FeedbackCrud.find_all(product_id=product_id)
