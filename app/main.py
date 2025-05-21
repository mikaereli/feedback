from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.feedback import router as feedback_router
from app.routers.product import router as product_router
from app.routers.user import router as user_router
from app.routers.purchase import router as purchase_router

app = FastAPI()

app.include_router(feedback_router)
app.include_router(product_router)
app.include_router(user_router)
app.include_router(purchase_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)