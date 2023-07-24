from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import FamilyCoreDatum, UpdateFamilyCoreDatum
from app.backend.classes.family_core_datum_class import FamilyCoreDatumClass

family_core_data = APIRouter(
    prefix="/family_core_data",
    tags=["Family_Core_Data"]
)

@family_core_data.get("/")
def index(db: Session = Depends(get_db)):
    data = FamilyCoreDatumClass(db).get_all()

    return {"message": data}

@family_core_data.post("/store")
def store(family_core_data:FamilyCoreDatum, db: Session = Depends(get_db)):
    family_type_inputs = family_core_data.dict()
    data = FamilyCoreDatumClass(db).store(family_type_inputs)

    return {"message": data}

@family_core_data.get("/edit/{id}")
def edit(id:int, db: Session = Depends(get_db)):
    data = FamilyCoreDatumClass(db).get("id", id)

    return {"message": data}

@family_core_data.delete("/delete/{id}")
def delete(id:int, db: Session = Depends(get_db)):
    data = FamilyCoreDatumClass(db).delete(id)

    return {"message": data}

@family_core_data.patch("/update/{id}")
def update(id: int, family_core_data: UpdateFamilyCoreDatum, db: Session = Depends(get_db)):
    data = FamilyCoreDatumClass(db).update(id, family_core_data)

    return {"message": data}