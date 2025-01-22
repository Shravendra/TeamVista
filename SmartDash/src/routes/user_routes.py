from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.utils.database import get_db
from src.dto.user_dto import UserCreate, UserResponse
from src.services import user_service

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)