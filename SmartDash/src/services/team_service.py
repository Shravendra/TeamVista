from sqlalchemy.orm import Session
from src.models.team import Team

def get_all_teams(db: Session):
    return db.query(Team).all()

def create_team(db: Session, team_data):
    team = Team(**team_data)
    db.add(team)
    db.commit()
    db.refresh(team)
    return team

def get_team_by_id(team_id: int, db: Session):
    return db.query(Team).filter(Team.id == team_id).first()

def delete_team(team_id: int, db: Session):
    team = get_team_by_id(team_id, db)
    if team:
        db.delete(team)
        db.commit()
    return team