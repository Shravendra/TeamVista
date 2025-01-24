from sqlalchemy.orm import Session
from src.models.employee import Employee
from src.dto.employee_dto import EmployeeCreate, EmployeeUpdate

def get_all_employee(db: Session):
    return db.query(Employee).all()

def create_employee(db: Session, employee_data: EmployeeCreate):
    # Convert Pydantic model to dict
    employee_dict = employee_data.model_dump()
    employee = Employee(**employee_dict)
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def get_employee_by_id(employee_id: int, db: Session):
    return db.query(Employee).filter(Employee.id == employee_id).first()

def update_employee(db: Session, employee_id: int, employee_data: EmployeeUpdate):
    employee = get_employee_by_id(employee_id, db)
    if employee:
        employee_dict = employee_data.model_dump(exclude_unset=True)
        for key, value in employee_dict.items():
            setattr(employee, key, value)
        db.commit()
        db.refresh(employee)
    return employee

def delete_employee(employee_id: int, db: Session):
    employee = get_employee_by_id(employee_id, db)
    if employee:
        db.delete(employee)
        db.commit()
    return employee