from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from src.utils.database import Base
from src.utils.constant import WorkStageEnum

class WorkStage(Base):
    __tablename__ = 'work_stages'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    stage = Column(SQLEnum(WorkStageEnum), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    
    # Stage details
    l4_zoning = Column(String, nullable=True)
    dp_placement = Column(String, nullable=True)
    snapping = Column(String, nullable=True)
    clustering = Column(String, nullable=True)
    cabling = Column(String, nullable=True)
    cat_survey_feedback = Column(String, nullable=True)
    artefacts = Column(String, nullable=True)
    validation = Column(String, nullable=True)
    
    # Relationships
    city = relationship("City", back_populates="work_stages")
    nbus = relationship("NBU", back_populates="stage")
    daily_updates = relationship("DailyUpdate", back_populates="stage")

class DailyUpdate(Base):
    __tablename__ = 'daily_updates'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    resource_count = Column(Integer, nullable=False)
    leave_count = Column(Integer, nullable=False)
    stage_id = Column(Integer, ForeignKey('work_stages.id'), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    
    stage = relationship("WorkStage", back_populates="daily_updates")
    team = relationship("Team", back_populates="daily_updates")

class ForecastData(Base):
    __tablename__ = 'forecast_data'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    month = Column(String, nullable=False)
    forecast_count = Column(Integer, nullable=False)
    stage = Column(SQLEnum(WorkStageEnum), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    
    team = relationship("Team", back_populates="forecasts")