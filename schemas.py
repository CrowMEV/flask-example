from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    


class UserCreate(User):
    password: str

class UserResponse(User):
    id: int