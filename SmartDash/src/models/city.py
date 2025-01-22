from sqlalchemy import Column, Integer, String
from src.utils.database import Base

class City(Base):
    __tablename__ = 'city'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    stage = Column(String, nullable=False)
    planner_name = Column(String, nullable=True)
    qa_name = Column(String, nullable=True)
    technical_reviewer = Column(String, nullable=True)