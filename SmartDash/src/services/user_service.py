from sqlalchemy.orm import Session
from src.models.user import User
from src.dto.user_dto import UserCreate
from src.services.auth_service import get_password_hash

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        password=hashed_password,
        role=user.role,
        team_id=user.team_id,
        tools_access=user.tools_access,
        score_card=user.score_card,
        attendance=user.attendance
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()