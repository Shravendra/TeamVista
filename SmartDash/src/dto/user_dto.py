from pydantic import BaseModel, validator
from typing import Optional

class UserBase(BaseModel):
    username: str
    role: str
    team_id: Optional[int] = None
    tools_access: Optional[str] = None
    score_card: Optional[str] = None
    attendance: Optional[str] = None

class UserCreate(UserBase):
    password: str

    @validator('role')
    def validate_role(cls, v):
        allowed_roles = ['SME', 'TL', 'Management']
        if v not in allowed_roles:
            raise ValueError(f'Role must be one of {allowed_roles}')
        return v

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True