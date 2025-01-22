from sqlalchemy.orm import Session
from src.models.work_stage import ForecastData

def get_all_forecasts(db: Session):
    return db.query(ForecastData).all()

def create_forecast(db: Session, forecast_data):
    forecast = ForecastData(**forecast_data)
    db.add(forecast)
    db.commit()
    db.refresh(forecast)
    return forecast

def get_forecast_by_id(forecast_id: int, db: Session):
    return db.query(ForecastData).filter(ForecastData.id == forecast_id).first()

def delete_forecast(forecast_id: int, db: Session):
    forecast = get_forecast_by_id(forecast_id, db)
    if forecast:
        db.delete(forecast)
        db.commit()
    return forecast