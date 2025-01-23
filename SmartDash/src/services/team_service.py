from sqlalchemy.orm import Session
from src.models.team import Team
from src.dto.team_dto import TeamCreate, TeamUpdate

def get_all_teams(db: Session):
    return db.query(Team).all()

def create_team(db: Session, team_data: TeamCreate):
    # Convert Pydantic model to dict
    team_dict = team_data.model_dump()
    team = Team(**team_dict)
    db.add(team)
    db.commit()
    db.refresh(team)
    return team

def get_team_by_id(team_id: int, db: Session):
    return db.query(Team).filter(Team.id == team_id).first()

def update_team(db: Session, team_id: int, team_data: TeamUpdate):
    team = get_team_by_id(team_id, db)
    if team:
        team_dict = team_data.model_dump(exclude_unset=True)
        for key, value in team_dict.items():
            setattr(team, key, value)
        db.commit()
        db.refresh(team)
    return team

def delete_team(team_id: int, db: Session):
    team = get_team_by_id(team_id, db)
    if team:
        db.delete(team)
        db.commit()
    return team