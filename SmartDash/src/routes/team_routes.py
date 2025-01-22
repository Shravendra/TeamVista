from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.utils.database import get_db
from src.models.team import Team
from src.dto.team_dto import TeamCreate, TeamResponse, TeamUpdate, EmployeeResponse, DailyTrackerResponse, ForecastResponse
from src.services import team_service

router = APIRouter()

@router.get("/", response_model=List[TeamResponse])
def get_teams(db: Session = Depends(get_db)):
    """Get all teams"""
    return team_service.get_all_teams(db)

@router.get("/{team_id}", response_model=TeamResponse)
def get_team(team_id: int, db: Session = Depends(get_db)):
    """Get a team by ID"""
    team = team_service.get_team_by_id(team_id, db)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@router.post("/", response_model=TeamResponse)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    """Create a new team"""
    return team_service.create_team(db, team)

@router.put("/{team_id}", response_model=TeamResponse)
def update_team(team_id: int, team: TeamUpdate, db: Session = Depends(get_db)):
    """Update a team"""
    existing_team = team_service.get_team_by_id(team_id, db)
    if not existing_team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team_service.update_team(db, team_id, team)

@router.delete("/{team_id}")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    """Delete a team"""
    existing_team = team_service.get_team_by_id(team_id, db)
    if not existing_team:
        raise HTTPException(status_code=404, detail="Team not found")
    team_service.delete_team(db, team_id)
    return {"message": "Team deleted successfully"}

@router.get("/{team_id}/employees", response_model=List[EmployeeResponse])
def get_team_employees(team_id: int, db: Session = Depends(get_db)):
    """Get all employees in a team"""
    team = team_service.get_team_by_id(team_id, db)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team.employees

@router.get("/{team_id}/daily-trackers", response_model=List[DailyTrackerResponse])
def get_team_daily_trackers(team_id: int, db: Session = Depends(get_db)):
    """Get all daily trackers for a team"""
    team = team_service.get_team_by_id(team_id, db)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team.daily_trackers

@router.get("/{team_id}/forecasts", response_model=List[ForecastResponse])
def get_team_forecasts(team_id: int, db: Session = Depends(get_db)):
    """Get all forecasts for a team"""
    team = team_service.get_team_by_id(team_id, db)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team.forecasts