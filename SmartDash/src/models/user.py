from sqlalchemy import Column, Integer, String, Date
from src.utils.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    employee_id = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=True)
    citrix_id = Column(String, unique=True, nullable=True)
    doj = Column(Date, nullable=False)
    dob = Column(Date, nullable=True)
    skills = Column(String, nullable=True)
    tools_access = Column(String, nullable=True)
    score_card = Column(String, nullable=True)
    attendance = Column(String, nullable=True)
