from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum as SQLEnum
from sqlalchemy.orm import relationship
from src.utils.database import Base
from src.utils.constant import TeamType

class Team(Base):
    __tablename__ = 'teams'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    type = Column(SQLEnum(TeamType), nullable=False)
    
    # Relationships
    users = relationship("User", back_populates="team")
    employees = relationship("Employee", back_populates="team")
    work_stages = relationship("WorkStage", back_populates="team")
    daily_trackers = relationship("DailyTracker", back_populates="team")
    forecasts = relationship("ForecastData", back_populates="team")
