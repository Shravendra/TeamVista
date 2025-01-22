from sqlalchemy.orm import Session
from src.models.work_stage import DailyTracker

def get_all_daily_trackers(db: Session):
    return db.query(DailyTracker).all()

def create_daily_tracker(db: Session, tracker_data):
    tracker = DailyTracker(**tracker_data)
    db.add(tracker)
    db.commit()
    db.refresh(tracker)
    return tracker

def get_daily_tracker_by_id(tracker_id: int, db: Session):
    return db.query(DailyTracker).filter(DailyTracker.id == tracker_id).first()

def delete_daily_tracker(tracker_id: int, db: Session):
    tracker = get_daily_tracker_by_id(tracker_id, db)
    if tracker:
        db.delete(tracker)
        db.commit()
    return tracker