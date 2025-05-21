from pydantic import BaseModel, EmailStr, ConfigDict

class SUserAuth(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(from_attributes=True)

class SUser(BaseModel):
    id: int
    email: EmailStr
    
    model_config = ConfigDict(from_attributes=True)