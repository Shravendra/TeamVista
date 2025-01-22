from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=True)
    tools_access = Column(String, nullable=True)
    score_card = Column(String, nullable=True)
    attendance = Column(String, nullable=True)
    
    team = relationship("Team", back_populates="users")