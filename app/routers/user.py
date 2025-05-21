from fastapi import APIRouter, Response, HTTPException, status
from typing import List

from app.auth.auth import get_password_hash, authenticate_user, create_access_token
from app.schemas.user import SUserAuth, SUser
from app.crud.user import UserCrud

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=SUser)
async def register_user(user_data: SUserAuth):
    existing_user = await UserCrud.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    hashed_password = get_password_hash(user_data.password)
    return await UserCrud.add(email=user_data.email, hashed_password=hashed_password)

@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token

@router.get("/", response_model=List[SUser])
async def get_users():
    return await UserCrud.find_all()