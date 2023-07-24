from app.backend.db.models import FamilyCoreDatumModel

class FamilyCoreDatumClass:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        try:
            data = self.db.query(FamilyCoreDatumModel).order_by(FamilyCoreDatumModel.id).all()
            if not data:
                return "No hay registros"
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def get(self, field, value):
        try:
            data = self.db.query(FamilyCoreDatumModel).filter(getattr(FamilyCoreDatumModel, field) == value).first()
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, family_core_datum_inputs):
        try:
            data = FamilyCoreDatumModel(**family_core_datum_inputs)
            self.db.add(data)
            self.db.commit()
            return "Registro agregado"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def delete(self, id):
        try:
            data = self.db.query(FamilyCoreDatumModel).filter(FamilyCoreDatumModel.id == id).first()
            if data:
                self.db.delete(data)
                self.db.commit()
                return "Registro eliminado"
            else:
                return "No se encontró el registro"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def update(self, id, family_core_datum):
        existing_family_core_datum = self.db.query(FamilyCoreDatumModel).filter(FamilyCoreDatumModel.id == id).one_or_none()

        if not existing_family_core_datum:
            return "No se encontró el registro"

        existing_family_type_core_datum_data = family_core_datum.dict(exclude_unset=True)
        for key, value in existing_family_type_core_datum_data.items():
            setattr(existing_family_core_datum, key, value)

        self.db.commit()

        return "Registro actualizado"