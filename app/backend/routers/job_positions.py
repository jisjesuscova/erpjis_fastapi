from fastapi import APIRouter, Depends
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.schemas import JobPosition, UpdateJobPosition
from app.backend.classes.job_position_class import JobPositionClass

job_positions = APIRouter(
    prefix="/job_positions",
    tags=["Job_Positions"]
)

@job_positions.get("/")
def index(db: Session = Depends(get_db)):
    data = JobPositionClass(db).get_all()

    return {"message": data}

@job_positions.post("/store")
def store(JobPosition:JobPosition, db: Session = Depends(get_db)):
    JobPosition_inputs = JobPosition.dict()
    data = JobPositionClass(db).store(JobPosition_inputs)

    return {"message": data}

@job_positions.get("/edit/{id}")
def edit(id:int, db: Session = Depends(get_db)):
    data = JobPositionClass(db).get("id", id)

    return {"message": data}

@job_positions.delete("/delete/{id}")
def delete(id:int, db: Session = Depends(get_db)):
    data = JobPositionClass(db).delete(id)

    return {"message": data}

@job_positions.patch("/update/{id}")
def update(id: int, JobPosition: UpdateJobPosition, db: Session = Depends(get_db)):
    data = JobPositionClass(db).update(id, JobPosition)

    return {"message": data}