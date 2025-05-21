from fastapi import APIRouter
from typing import List

from app.schemas.product import SProductCreate, SProduct
from app.crud.product import ProductCrud

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=SProduct)
async def add_product(product_data: SProductCreate):
    return await ProductCrud.add(**product_data.model_dump())


@router.get("/", response_model=List[SProduct])
async def get_products():
    return await ProductCrud.find_all()
