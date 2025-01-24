from pydantic import BaseModel, validator
from typing import List, Optional
from datetime import date



class EmployeeBase(BaseModel):
    name: str
    employee_id: str
    enterprise_id: str
    address: Optional[str] = None
    citrix_id: Optional[str] = None

class EmployeeCreate(EmployeeBase):
    team_id: int

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int
    team_id: int

    class Config:
        from_attributes = True