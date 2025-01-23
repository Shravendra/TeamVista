from sqlalchemy import Column, Integer, String, Enum as SQLEnum
from sqlalchemy.orm import relationship

from src.utils.database import Base
from src.utils.constant import WorkStageEnum

class City(Base):
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    stage = Column(String, nullable=False)
    planner_name = Column(String, nullable=True)
    qa_name = Column(String, nullable=True)
    city_zoning = Column(SQLEnum(WorkStageEnum), nullable=False)
    technical_reviewer = Column(String, nullable=True)

    work_stages = relationship("WorkStage", back_populates="city")