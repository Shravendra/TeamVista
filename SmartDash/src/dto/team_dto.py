from pydantic import BaseModel, validator
from typing import List, Optional
from datetime import date

class TeamBase(BaseModel):
    name: str

    @validator('name')
    def name_must_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Team name cannot be empty')
        return v.strip()

class TeamCreate(TeamBase):
    pass

class TeamUpdate(TeamBase):
    name: Optional[str] = None

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

class DailyTrackerBase(BaseModel):
    date: date
    activity_details: str
    team_id: int
    employee_id: int

class DailyTrackerResponse(DailyTrackerBase):
    id: int

    class Config:
        from_attributes = True

class ForecastBase(BaseModel):
    month: str
    forecast_count: int
    team_id: int

class ForecastResponse(ForecastBase):
    id: int

    class Config:
        from_attributes = True

class TeamResponse(TeamBase):
    id: int
    employees: List[EmployeeResponse] = []
    daily_trackers: List[DailyTrackerResponse] = []
    forecasts: List[ForecastResponse] = []

    class Config:
        from_attributes = True