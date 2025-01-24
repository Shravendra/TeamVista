from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from src.utils.database import Base


class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    employee_id = Column(String, unique=True, nullable=False)
    enterprise_id = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=True)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=True)
    doj = Column(Date, nullable=True)
    dob = Column(Date, nullable=True)
    skills = Column(String, nullable=True)
    tools_access = Column(String, nullable=True)
    score_card = Column(String, nullable=True)
    attendance = Column(String, nullable=True)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    
    # Relationships
    team = relationship("Team", back_populates="employees")
    city = relationship("City", back_populates="city_employees")
    daily_trackers = relationship("DailyTracker", back_populates="employee")