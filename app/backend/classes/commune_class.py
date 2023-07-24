from app.backend.db.models import CommuneModel

class CommuneClass:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        try:
            data = self.db.query(CommuneModel).order_by(CommuneModel.id).all()
            if not data:
                return "No hay registros"
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def get(self, field, value):
        try:
            data = self.db.query(CommuneModel).filter(getattr(CommuneModel, field) == value).first()
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, commune_inputs):
        try:
            data = CommuneModel(**commune_inputs)
            self.db.add(data)
            self.db.commit()
            return 1
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def delete(self, id):
        try:
            data = self.db.query(CommuneModel).filter(CommuneModel.id == id).first()
            if data:
                self.db.delete(data)
                self.db.commit()
                return "Registro eliminado"
            else:
                return "No se encontró el registro"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def update(self, id, commune):
        existing_commune = self.db.query(CommuneModel).filter(CommuneModel.id == id).one_or_none()

        if not existing_commune:
            return "No se encontró el registro"

        existing_commune_data = commune.dict(exclude_unset=True)
        for key, value in existing_commune_data.items():
            setattr(existing_commune, key, value)

        self.db.commit()

        return "Registro actualizado"