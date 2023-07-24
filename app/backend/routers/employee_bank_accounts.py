from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import EmployeeBankAccount, UpdateEmployeeBankAccount
from app.backend.classes.employee_bank_account_class import EmployeeBankAccountClass

employee_bank_accounts = APIRouter(
    prefix="/employee_bank_accounts",
    tags=["EmployeeBankAccounts"]
)

@employee_bank_accounts.get("/")
def index(db: Session = Depends(get_db)):
    data = EmployeeBankAccountClass(db).get_all()

    return {"message": data}

@employee_bank_accounts.post("/store")
def store(bank:EmployeeBankAccount, db: Session = Depends(get_db)):
    bank_inputs = bank.dict()
    data = EmployeeBankAccountClass(db).store(bank_inputs)

    return {"message": data}

@employee_bank_accounts.get("/edit/{id}")
def edit(id:int, db: Session = Depends(get_db)):
    data = EmployeeBankAccountClass(db).get("id", id)

    return {"message": data}

@employee_bank_accounts.delete("/delete/{id}")
def delete(id:int, db: Session = Depends(get_db)):
    data = EmployeeBankAccountClass(db).delete(id)

    return {"message": data}

@employee_bank_accounts.patch("/update/{id}")
def update(id: int, employee_bank_account: UpdateEmployeeBankAccount, db: Session = Depends(get_db)):
    data = EmployeeBankAccountClass(db).update(id, employee_bank_account)

    return {"message": data}