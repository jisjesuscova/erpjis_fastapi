from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import Principal, UpdatePrincipal
from app.backend.classes.principal_class import PrincipalClass

principals = APIRouter(
    prefix="/principals",
    tags=["Principals"]
)

@principals.get("/")
def index(db: Session = Depends(get_db)):
    data = PrincipalClass(db).get_all()

    return {"message": data}

@principals.post("/store")
def store(principal:Principal, db: Session = Depends(get_db)):
    principal_inputs = principal.dict()
    data = PrincipalClass(db).store(principal_inputs)

    return {"message": data}

@principals.get("/edit/{id}")
def edit(id:int, db: Session = Depends(get_db)):
    data = PrincipalClass(db).get("id", id)

    return {"message": data}

@principals.delete("/delete/{id}")
def delete(id:int, db: Session = Depends(get_db)):
    data = PrincipalClass(db).delete(id)

    return {"message": data}

@principals.patch("/update/{id}")
def update(id: int, principal: UpdatePrincipal, db: Session = Depends(get_db)):
    data = PrincipalClass(db).update(id, principal)

    return {"message": data}