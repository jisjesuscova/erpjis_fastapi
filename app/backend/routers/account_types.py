from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.db.models import AccountTypeModel
from app.backend.schemas import AccountType, UpdateAccountType

account_types = APIRouter(
    prefix="/account_types",
    tags=["Account_Types"]
)

@account_types.get("/")
def index(db: Session = Depends(get_db)):
    data = db.query(AccountTypeModel).all()

    return {"message": data}

@account_types.post("/store")
def store(account_type:AccountType, db: Session = Depends(get_db)):
    account_type_inputs = account_type.dict()
    data = AccountTypeModel(**account_type_inputs)

    db.add(data)
    db.commit()

    return {"message": data}

@account_types.get("/edit/{id}")
def edit(id:int, db: Session = Depends(get_db)):
    data = db.query(AccountTypeModel).filter(AccountTypeModel.id == id).first()

    return {"message": data}

@account_types.delete("/delete/{id}")
def delete(id:int, db: Session = Depends(get_db)):
    data = db.query(AccountTypeModel).filter(AccountTypeModel.id == id)

    if not data.first():
        return {"message": "Banco no encontrado!"}
    
    data.delete(synchronize_session=False)

    db.commit()

    return {"message": "Banco eliminado!"}

@account_types.patch("/update/{id}")
def store(id:int, account_type:UpdateAccountType, db: Session = Depends(get_db)):
    data = db.query(AccountTypeModel).filter(AccountTypeModel.id == id)

    if not data.first():
        return {"message": "Banco no encontrado!"}
    
    data.update(account_type.dict(exclude_unset=True))

    db.commit()

    return {"message": data}