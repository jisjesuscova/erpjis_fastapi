from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.db.models import AlertTypeModel
from app.backend.schemas import AlertType, UpdateAlertType

alert_types = APIRouter(
    prefix="/alert_types",
    tags=["Alert_Types"]
)

@alert_types.get("/")
def index(db: Session = Depends(get_db)):
    data = db.query(AlertTypeModel).all()

    return {"message": data}

@alert_types.post("/store")
def store(alert_type:AlertType, db: Session = Depends(get_db)):
    alert_type_inputs = alert_type.dict()
    data = AlertTypeModel(**alert_type_inputs)

    db.add(data)
    db.commit()

    return {"message": data}

@alert_types.get("/edit/{id}")
def edit(id:int, db: Session = Depends(get_db)):
    data = db.query(AlertTypeModel).filter(AlertTypeModel.id == id).first()

    return {"message": data}

@alert_types.delete("/delete/{id}")
def delete(id:int, db: Session = Depends(get_db)):
    data = db.query(AlertTypeModel).filter(AlertTypeModel.id == id)

    if not data.first():
        return {"message": "Tipo de alerta no encontrada!"}
    
    data.delete(synchronize_session=False)

    db.commit()

    return {"message": "Tipo de alerta eliminada!"}

@alert_types.patch("/update/{id}")
def store(id:int, alert_type:UpdateAlertType, db: Session = Depends(get_db)):
    data = db.query(AlertTypeModel).filter(AlertTypeModel.id == id)

    if not data.first():
        return {"message": "Tipo de alerta no encontrada!"}
    
    data.update(alert_type.dict(exclude_unset=True))

    db.commit()

    return {"message": data}