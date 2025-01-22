from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.utils.database import get_db
from src.models.city import City
from src.dto.city_dto import CityCreate, CityResponse, CityUpdate, WorkStageResponse
from src.services import city_service

router = APIRouter()

@router.get("/", response_model=List[CityResponse])
def get_cities(db: Session = Depends(get_db)):
    """Get all cities"""
    return city_service.get_all_cities(db)

@router.get("/{city_id}", response_model=CityResponse)
def get_city(city_id: int, db: Session = Depends(get_db)):
    """Get a city by ID"""
    city = city_service.get_city_by_id(city_id, db)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@router.post("/", response_model=CityResponse)
def create_city(city: CityCreate, db: Session = Depends(get_db)):
    """Create a new city"""
    return city_service.create_city(db, city)

@router.put("/{city_id}", response_model=CityResponse)
def update_city(city_id: int, city: CityUpdate, db: Session = Depends(get_db)):
    """Update a city"""
    existing_city = city_service.get_city_by_id(city_id, db)
    if not existing_city:
        raise HTTPException(status_code=404, detail="City not found")
    return city_service.update_city(db, city_id, city)

@router.delete("/{city_id}")
def delete_city(city_id: int, db: Session = Depends(get_db)):
    """Delete a city"""
    existing_city = city_service.get_city_by_id(city_id, db)
    if not existing_city:
        raise HTTPException(status_code=404, detail="City not found")
    city_service.delete_city(db, city_id)
    return {"message": "City deleted successfully"}

@router.get("/{city_id}/stages", response_model=List[WorkStageResponse])
def get_city_stages(city_id: int, db: Session = Depends(get_db)):
    """Get all work stages for a city"""
    city = city_service.get_city_by_id(city_id, db)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city_service.get_city_stages(db, city_id)

@router.get("/stage/{stage_name}", response_model=List[CityResponse])
def get_cities_by_stage(stage_name: str, db: Session = Depends(get_db)):
    """Get all cities in a specific stage"""
    return city_service.get_cities_by_stage(db, stage_name)

@router.get("/{city_id}/details", response_model=CityResponse)
def get_city_details(city_id: int, db: Session = Depends(get_db)):
    """Get detailed information about a city including all work stages"""
    city = city_service.get_city_details(db, city_id)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city