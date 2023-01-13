from config import schemas,models,database,user
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

router = APIRouter(
    prefix='/user'
)

get_db = database.get_db

@router.get('/',response_model=List[schemas.UserShowBase])
def all(db:Session=Depends(get_db)):
    return user.get_all(db)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request:schemas.UserBase,db:Session=Depends(get_db)):
    return user.create(request,db)

@router.get("/{id}",response_model=schemas.UserShowBase)
def get_id(id:int,db:Session=Depends(get_db)):
    return user.get_by_id(db,id)

@router.post("/{id}",status_code=status.HTTP_201_CREATED,response_model=schemas.UserShowBase)
def update(request:schemas.UserBase,id:int,db:Session=Depends(get_db)):
    return user.update(request,id,db)