from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.database import Base

class Team(Base):
    __tablename__ = 'teams'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    
    users = relationship("User", back_populates="team")
    employees = relationship("Employee", back_populates="team")
    daily_trackers = relationship("DailyTracker", back_populates="team")
    forecasts = relationship("ForecastData", back_populates="team")

class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    employee_id = Column(String, unique=True, nullable=False)
    enterprise_id = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=True)
    citrix_id = Column(String, unique=True, nullable=True)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    
    team = relationship("Team", back_populates="employees")
    daily_trackers = relationship("DailyTracker", back_populates="employee")