from sqlalchemy.orm import Session
from src.models.city import City

def get_all_cities(db: Session):
    return db.query(City).all()

def create_city(db: Session, city_data):
    city = City(**city_data)
    db.add(city)
    db.commit()
    db.refresh(city)
    return city

def get_city_by_id(city_id: int, db: Session):
    return db.query(City).filter(City.id == city_id).first()

def delete_city(city_id: int, db: Session):
    city = get_city_by_id(city_id, db)
    if city:
        db.delete(city)
        db.commit()
    return city
