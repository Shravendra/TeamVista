from pydantic import BaseModel, validator
from datetime import date

class UserCreate(BaseModel):
    username: str
    password: str
    role: str
    team_id: int

    @validator('role')
    def role_must_be_valid(cls, v):
        if v not in ['SME', 'TL', 'Management']:
            raise ValueError('Invalid role')
        return v

class DailyTrackerCreate(BaseModel):
    date: date
    activity_details: str
    team_id: int
    employee_id: int

    @validator('date')
    def date_must_be_in_past(cls, v):
        if v > date.today():
            raise ValueError('Date cannot be in the future')
        return v

class ForecastCreate(BaseModel):
    month: str
    forecast_count: int
    team_id: int

    @validator('forecast_count')
    def forecast_count_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('Forecast count must be positive')
        return v