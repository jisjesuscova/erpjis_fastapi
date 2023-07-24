from app.backend.db.models import JobPositionModel

class JobPositionClass:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        try:
            data = self.db.query(JobPositionModel).order_by(JobPositionModel.id).all()
            if not data:
                return "No hay registros"
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def get(self, field, value):
        try:
            data = self.db.query(JobPositionModel).filter(getattr(JobPositionModel, field) == value).first()
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, JobPosition_inputs):
        try:
            data = JobPositionModel(**JobPosition_inputs)
            self.db.add(data)
            self.db.commit()
            return "Registro agregado"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def delete(self, id):
        try:
            data = self.db.query(JobPositionModel).filter(JobPositionModel.id == id).first()
            if data:
                self.db.delete(data)
                self.db.commit()
                return "Registro eliminado"
            else:
                return "No se encontró el registro"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def update(self, id, JobPosition):
        existing_job_position = self.db.query(JobPositionModel).filter(JobPositionModel.id == id).one_or_none()

        if not existing_job_position:
            return "No se encontró el registro"

        existing_job_position_type_data = JobPosition.dict(exclude_unset=True)
        for key, value in existing_job_position_type_data.items():
            setattr(existing_job_position, key, value)

        self.db.commit()

        return "Registro actualizado"