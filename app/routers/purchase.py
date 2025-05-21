from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from app.schemas.purchase import SPurchaseCreate, SPurchase
from app.crud.purchase import PurchaseCrud
from app.crud.product import ProductCrud
from app.auth.dependecies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/purchases", tags=["Purchases"])

@router.post("/", response_model=SPurchase)
async def purchase_product(purchase_data: SPurchaseCreate, current_user: User = Depends(get_current_user)):
    # Check if product exists
    product = await ProductCrud.find_one_or_none(id=purchase_data.product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    # Check if there's enough quantity available
    if product.get("amount", 0) < purchase_data.quantity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough product quantity available"
        )
    
    # Create the purchase
    purchase = await PurchaseCrud.add(
        user_id=current_user.id,
        product_id=purchase_data.product_id,
        quantity=purchase_data.quantity
    )
    
    # Update product quantity
    new_amount = product.get("amount", 0) - purchase_data.quantity
    await ProductCrud.update(id=purchase_data.product_id, amount=new_amount)
    
    return purchase

@router.get("/my", response_model=List[SPurchase])
async def get_my_purchases(current_user: User = Depends(get_current_user)):
    return await PurchaseCrud.get_user_purchases(current_user.id)
