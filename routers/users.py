from fastapi import FastAPI, Depends, HTTPException, Path, APIRouter
from models import users 
from passlib.context import CryptContext
from typing import Annotated
from database import SessionLocal
from sqlalchemy.orm import Session
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt,JWTError
from datetime import timedelta, datetime
from routers.auth import get_current_user
from pydantic import BaseModel, Field


router = APIRouter(
    prefix='/Users',
    tags=['Users']
)

class Verification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

@router.get('/users', status_code=status.HTTP_200_OK)
async def get_users(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,  detail='Authentication Failed')
    db_users = db.query(users).filter(users.id == user.get('id')).first()
    return db_users

@router.post('/change_password', status_code=status.HTTP_200_OK)
async def change_password(user: user_dependency, db: db_dependency, 
                        user_password: Verification):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_model = db.query(users).filter(users.id == user.get('id')).first()

    if not bcrypt_context.verify(user_password.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail='Error on password change')
    user_model.hashed_password = bcrypt_context.hash(user_password.new_password)

    db.add(user_model)
    db.commit()

@router.post('/change_phone_number', status_code=status.HTTP_200_OK)
async def change_phone_number(user: user_dependency, db: db_dependency, 
                        phone_number: str):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_model = db.query(users).filter(users.id == user.get('id')).first()
    user_model.phone_number = phone_number
    db.add(user_model)
    db.commit()