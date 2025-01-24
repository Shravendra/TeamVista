from pydantic import BaseModel, validator
from typing import List, Optional
from datetime import date
from src.utils.constant import TeamType
from src.dto.employee_dto import EmployeeResponse


class TeamBase(BaseModel):
    name: str
    type: TeamType

    @validator('name')
    def name_must_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Team name cannot be empty')
        return v.strip()

    @validator('type')
    def validate_team_type(cls, v):
        if not isinstance(v, TeamType):
            raise ValueError(f'Invalid team type. Must be one of {[t.value for t in TeamType]}')
        return v

class TeamCreate(TeamBase):
    pass


class TeamUpdate(TeamBase):
    name: Optional[str] = None
    type: Optional[TeamType] = None


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

    class Config:
        from_attributes = True