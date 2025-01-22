from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.utils.database import get_db
from src.services.auth_service import verify_password, create_access_token
from src.models.user import User

router = APIRouter()

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/mfa")
def verify_mfa(mfa_code: str):
    # Implement MFA verification logic here
    pass

@router.get("/logout")
def logout():
    # Implement logout logic here
    pass