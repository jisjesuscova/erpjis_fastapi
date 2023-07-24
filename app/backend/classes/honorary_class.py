from app.backend.db.models import HonoraryModel

class HonoraryClass:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        try:
            data = self.db.query(HonoraryModel).order_by(HonoraryModel.id).all()
            if not data:
                return "No hay registros"
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def get(self, field, value):
        try:
            data = self.db.query(HonoraryModel).filter(getattr(HonoraryModel, field) == value).first()
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, Honorary_inputs):
        try:
            data = HonoraryModel(**Honorary_inputs)
            self.db.add(data)
            self.db.commit()
            return "Registro agregado"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def delete(self, id):
        try:
            data = self.db.query(HonoraryModel).filter(HonoraryModel.id == id).first()
            if data:
                self.db.delete(data)
                self.db.commit()
                return "Registro eliminado"
            else:
                return "No se encontró el registro"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def update(self, id, Honorary):
        existing_honorary = self.db.query(HonoraryModel).filter(HonoraryModel.id == id).one_or_none()

        if not existing_honorary:
            return "No se encontró el registro"

        existing_honorary_data = Honorary.dict(exclude_unset=True)
        for key, value in existing_honorary_data.items():
            setattr(existing_honorary, key, value)

        self.db.commit()

        return "Registro actualizado"