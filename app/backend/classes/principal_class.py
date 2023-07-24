from app.backend.db.models import PrincipalModel

class PrincipalClass:
    def __init__(self, db):
        self.db = db
    
    def get(self, field, value):
        try:
            data = self.db.query(PrincipalModel).filter(getattr(PrincipalModel, field) == value).first()
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, principal_inputs):
        try:
            data = PrincipalModel(**principal_inputs)
            self.db.add(data)
            self.db.commit()
            return "Registro agregado"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def delete(self, id):
        try:
            data = self.db.query(PrincipalModel).filter(PrincipalModel.id == id).first()
            if data:
                self.db.delete(data)
                self.db.commit()
                return "Registro eliminado"
            else:
                return "No se encontró el registro"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def update(self, id, principal):
        existing_principal = self.db.query(PrincipalModel).filter(PrincipalModel.id == id).one_or_none()

        if not existing_principal:
            return "No se encontró el registro"

        existing_principal_data = principal.dict(exclude_unset=True)
        for key, value in existing_principal_data.items():
            setattr(existing_principal, key, value)

        self.db.commit()

        return "Registro actualizado"