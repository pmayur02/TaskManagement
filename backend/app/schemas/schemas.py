from pydantic import BaseModel, EmailStr
from typing import Optional
class UserModel(BaseModel):
    name : str
    email : EmailStr
    password : str
    role :Optional[str] = "User"
    isActive : Optional[bool] = True

    class Config():
        orm_mode = True

class UserResponseModel(BaseModel): 
    data:list
    message:str
    status:int


class TaskModel(BaseModel):
    title: str
    taskDetail: str

    class Config:
        orm_mode = True

class UpdateTaskModel(BaseModel):
    title: Optional[str] = None
    taskDetail: Optional[str] = None

    class Config:
        orm_mode = True


class LoginModel(BaseModel):
    email:str
    password:str

    class Config():
        orm_mode = True

class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    email: str | None = None
