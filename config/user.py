from config import schemas,models
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def get_all(db: Session):
    users = db.query(models.UserModel).all()
    return users

def get_by_id(db:Session,id:int):
    user = db.query(models.UserModel).filter(models.UserModel.id==id).first()
    return user

def create(request:schemas.UserBase,db:Session):
    new_user = models.UserModel(name=request.name,email=request.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update(request:schemas.UserBase,id:int,db:Session):
    update_user = models.UserModel(id=id,name=request.name,email=request.email)
    db.add(update_user)
    db.commit()
    db.refresh(update_user)
    return update_user