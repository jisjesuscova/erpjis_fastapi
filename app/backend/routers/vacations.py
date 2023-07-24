from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import Vacation
from app.backend.classes.vacation_class import VacationClass
from app.backend.classes.document_employee_class import DocumentEmployeeClass
from app.backend.classes.dropbox_class import DropboxClass

vacations = APIRouter(
    prefix="/vacations",
    tags=["Vacations"]
)

@vacations.get("/")
def index(db: Session = Depends(get_db)):
    data = VacationClass(db).get_all()

    return {"message": data}

@vacations.get("/total_vacation_days_in_company")
def total_vacation_days_in_company(db: Session = Depends(get_db)):
    data = VacationClass(db).calculate_total_vacation_days()

    return {"message": data}

@vacations.post("/store")
def store(vacation:Vacation, db: Session = Depends(get_db)):
    vacation_inputs = vacation.dict()

    document_id = DocumentEmployeeClass(db).store(vacation_inputs)
    vacation_inputs['document_employee_id'] = document_id
    vacation_data = VacationClass(db).store(vacation_inputs)

    return {"document_message": document_id,
            "vacation_message": vacation_data
        }

@vacations.delete("/delete/{id}")
def delete(id:int, db: Session = Depends(get_db)):
    document_employee_id = VacationClass(db).delete(id)
    document_employee = DocumentEmployeeClass(db).get("id", document_employee_id)
    response = DocumentEmployeeClass(db).delete(id)

    if response == 1:
        response = DropboxClass(db).delete('/vacations/', document_employee.support)

        if response == 1:
            data = 1
        else:
            data = 0
    else:
        data = 0
    
    return {"message": data}

@vacations.get("/legal/{rut}")
def legal(rut: int, db: Session = Depends(get_db)):
    data = VacationClass(db).legal(rut)

    return {"message": data}

@vacations.get("/taken/{rut}")
def taken(rut: int, db: Session = Depends(get_db)):
    data = VacationClass(db).taken(rut)

    return {"message": data}

@vacations.get("/balance/{legal}/{taken}")
def balance(legal: int, taken: int, db: Session = Depends(get_db)):
    data = VacationClass(db).balance(legal, taken)

    return {"message": data}
