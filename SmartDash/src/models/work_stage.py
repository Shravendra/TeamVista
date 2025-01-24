from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from src.utils.database import Base
from src.utils.constant import WorkStageEnum

class WorkStage(Base):
    __tablename__ = 'work_stages'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    stage = Column(SQLEnum(WorkStageEnum), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=True)
    
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
    team = relationship("Team", back_populates="work_stages")
    daily_trackers = relationship("DailyTracker", back_populates="stage")

class DailyTracker(Base):
    __tablename__ = 'daily_trackers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    resource_count = Column(Integer, nullable=False)
    leave_count = Column(Integer, nullable=False)
    details = Column(String, nullable=True)
    stage_id = Column(Integer, ForeignKey('work_stages.id'), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    
    stage = relationship("WorkStage", back_populates="daily_trackers")
    team = relationship("Team", back_populates="daily_trackers")
    employee = relationship("Employee", back_populates="daily_trackers")


class ForecastData(Base):
    __tablename__ = 'forecast_data'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    month = Column(String, nullable=False)
    forecast_count = Column(Integer, nullable=False)
    stage = Column(SQLEnum(WorkStageEnum), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    
    team = relationship("Team", back_populates="forecasts")