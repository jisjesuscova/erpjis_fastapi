from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import ContractDatum
from app.backend.classes.document_employee_class import DocumentEmployeeClass
from app.backend.classes.dropbox_class import DropboxClass

contract_data = APIRouter(
    prefix="/contract_data",
    tags=["ContractData"]
)

@contract_data.get("/")
def index(db: Session = Depends(get_db)):
    data = DocumentEmployeeClass(db).get_all()

    return {"message": data}

@contract_data.post("/store")
def store(contract_datum:ContractDatum, db: Session = Depends(get_db)):
    contract_datum_inputs = contract_datum.dict()
    document_id = DocumentEmployeeClass(db).store(contract_datum_inputs)

    return {"document_message": document_id}

@contract_data.delete("/delete/{id}")
def delete(id:int, db: Session = Depends(get_db)):
    document_employee = DocumentEmployeeClass(db).get("id", id)
    response = DocumentEmployeeClass(db).delete(id)

    if response == 1:
        response = DropboxClass(db).delete('/contracts/', document_employee.support)

        if response == 1:
            data = 1
        else:
            data = 0
    else:
        data = 0
    
    return {"message": data}