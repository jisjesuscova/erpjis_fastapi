from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import MedicalLicense, UpdateMedicalLicense, UserLogin
from app.backend.classes.medical_license_class import MedicalLicenseClass
from app.backend.auth.auth_user import get_current_active_user

medical_licenses = APIRouter(
    prefix="/medical_licenses",
    tags=["MedicalLicenses"]
)

@medical_licenses.get("/")
def index(session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = MedicalLicenseClass(db).get_all()

    return {"message": data}

@medical_licenses.post("/store")
def store(medical_license:MedicalLicense, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    medical_license_inputs = medical_license.dict()
    data = MedicalLicenseClass(db).store(medical_license_inputs)

    return {"message": data}

@medical_licenses.get("/edit/{id}")
def edit(id:int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = MedicalLicenseClass(db).get("id", id)

    return {"message": data}

@medical_licenses.delete("/delete/{id}")
def delete(id:int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = MedicalLicenseClass(db).delete(id)

    return {"message": data}

@medical_licenses.patch("/update/{id}")
def update(id: int, medical_license: UpdateMedicalLicense, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = MedicalLicenseClass(db).update(id, medical_license)

    return {"message": data}