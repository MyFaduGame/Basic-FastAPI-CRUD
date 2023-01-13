from pydantic import BaseModel
from config.database import Base

class UserBase(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True

class UserShowBase(BaseModel):
    name:str
    email:str

    class Config():
        orm_mode = True