from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import Honorary, UpdateHonorary, UserLogin
from app.backend.classes.honorary_class import HonoraryClass
from app.backend.auth.auth_user import get_current_active_user

honoraries = APIRouter(
    prefix="/honoraries",
    tags=["Honoraries"]
)

@honoraries.get("/")
def index(session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = HonoraryClass(db).get_all()

    return {"message": data}

@honoraries.post("/store")
def store(Honorary:Honorary, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    Honorary_inputs = Honorary.dict()
    data = HonoraryClass(db).store(Honorary_inputs)

    return {"message": data}

@honoraries.get("/edit/{id}")
def edit(id:int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = HonoraryClass(db).get("id", id)

    return {"message": data}

@honoraries.delete("/delete/{id}")
def delete(id:int, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = HonoraryClass(db).delete(id)

    return {"message": data}

@honoraries.patch("/update/{id}")
def update(id: int, honorary: UpdateHonorary, session_user: UserLogin = Depends(get_current_active_user), db: Session = Depends(get_db)):
    data = HonoraryClass(db).update(id, honorary)

    return {"message": data}