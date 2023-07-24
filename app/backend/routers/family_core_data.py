from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import FamilyCoreDatum, UpdateFamilyCoreDatum, UserLogin
from app.backend.classes.family_core_datum_class import FamilyCoreDatumClass
from app.backend.auth.auth_user import get_current_active_user
import os
from app.backend.classes.dropbox_class import DropboxClass

family_core_data = APIRouter(
    prefix="/family_core_data",
    tags=["Family_Core_Data"]
)

@family_core_data.get("/")
def index(session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = FamilyCoreDatumClass(db).get_all()

    return {"message": data}

@family_core_data.post("/store")
def store(form_data: FamilyCoreDatum = Depends(FamilyCoreDatum), session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    dropbox_client = DropboxClass(db)

    filename = dropbox_client.upload(name=form_data.rut, description='partida_nacimiento', data=form_data.support,
                                 dropbox_path='/intranet_jisparking_files/', computer_path=os.path.join('C:\\', 'Users', 'jesus', 'OneDrive', 'Desktop', 'erpjis_fastapi', 'app', 'backend'))

    data = FamilyCoreDatumClass(db).store(form_data, filename)

    return {"message": data}

@family_core_data.get("/edit/{id}")
def edit(id:int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = FamilyCoreDatumClass(db).get("id", id)

    return {"message": data}

@family_core_data.delete("/delete/{id}")
def delete(id:int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    family_core_data = FamilyCoreDatumClass(db).get("id", id)

    response = FamilyCoreDatumClass(db).delete(id)

    if response == 1:
        response = DropboxClass(db).delete('/intranet_jisparking_files/', family_core_data.support)

        if response == 1:
            data = 1
        else:
            data = response
    else:
        data = 0
    
    return {"message": data}

@family_core_data.patch("/update/{id}")
def update(id: int, form_data: UpdateFamilyCoreDatum = Depends(UpdateFamilyCoreDatum), session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    family_core_data = FamilyCoreDatumClass(db).get("id", id)

    if form_data.support != None:
        dropbox_client = DropboxClass(db)

        support = dropbox_client.upload(name=form_data.rut, description='partida_nacimiento', data=form_data.support,
                                 dropbox_path='/intranet_jisparking_files/', computer_path=os.path.join('C:\\', 'Users', 'jesus', 'OneDrive', 'Desktop', 'erpjis_fastapi', 'app', 'backend'))

        DropboxClass(db).delete('/intranet_jisparking_files/', str(family_core_data.support))
    
    data = FamilyCoreDatumClass(db).update(id, family_core_data, support)

    return {"message": data}