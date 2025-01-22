from sqlalchemy.orm import Session
from src.models.work_stage import WorkStage

def get_all_work_stages(db: Session):
    return db.query(WorkStage).all()

def create_work_stage(db: Session, work_stage_data):
    work_stage = WorkStage(**work_stage_data)
    db.add(work_stage)
    db.commit()
    db.refresh(work_stage)
    return work_stage

def get_work_stage_by_id(stage_id: int, db: Session):
    return db.query(WorkStage).filter(WorkStage.id == stage_id).first()

def update_work_stage(stage_id: int, db: Session, updated_data):
    stage = get_work_stage_by_id(stage_id, db)
    if stage:
        for key, value in updated_data.items():
            setattr(stage, key, value)
        db.commit()
        db.refresh(stage)
    return stage

def delete_work_stage(stage_id: int, db: Session):
    stage = get_work_stage_by_id(stage_id, db)
    if stage:
        db.delete(stage)
        db.commit()
    return stage
