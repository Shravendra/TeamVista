from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.utils.database import get_db
from src.dto.employee_dto import EmployeeCreate, EmployeeResponse, EmployeeUpdate
from src.services import employee_service

router = APIRouter()


@router.post("/", response_model=EmployeeResponse)
def create_employee(Employee: EmployeeCreate, db: Session = Depends(get_db)):
    """Create a new Employee"""
    return employee_service.create_employee(db, Employee)

@router.get("/", response_model=List[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    """Get all Employee"""
    return employee_service.get_all_employees(db)

@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    """Get a Employee by ID"""
    employee = employee_service.get_employee_by_id(employee_id, db)
    if not employee:
        raise HTTPException(status_code=404, detail="employee not found")
    return employee

@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    """Update a Employee"""
    existing_employee = employee_service.get_employee_by_id(employee_id, db)
    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee_service.update_employee(db, employee_id, employee)

@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    """Delete a Employee"""
    existing_employee = employee_service.get_employee_by_id(employee_id, db)
    if not existing_employee:
        raise HTTPException(status_code=404, detail="employee not found")
    employee_service.delete_employee(db, employee_id)
    return {"message": "Employee deleted successfully"}