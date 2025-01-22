from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.database import Base

class DailyTracker(Base):
    __tablename__ = 'daily_trackers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    activity_details = Column(String, nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    
    team = relationship("Team", back_populates="daily_trackers")
    employee = relationship("Employee", back_populates="daily_trackers")

class ForecastData(Base):
    __tablename__ = 'forecast_data'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    month = Column(String, nullable=False)
    forecast_count = Column(Integer, nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    
    team = relationship("Team", back_populates="forecasts")