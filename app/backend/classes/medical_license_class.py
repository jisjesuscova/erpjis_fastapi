from app.backend.db.models import MedicalLicenseModel

class MedicalLicenseClass:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        try:
            data = self.db.query(MedicalLicenseModel).order_by(MedicalLicenseModel.id).all()
            if not data:
                return "No hay registros"
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def get(self, field, value):
        try:
            data = self.db.query(MedicalLicenseModel).filter(getattr(MedicalLicenseModel, field) == value).first()
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, MedicalLicense_inputs):
        try:
            data = MedicalLicenseModel(**MedicalLicense_inputs)
            self.db.add(data)
            self.db.commit()
            return "Registro agregado"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def delete(self, id):
        try:
            data = self.db.query(MedicalLicenseModel).filter(MedicalLicenseModel.id == id).first()
            if data:
                self.db.delete(data)
                self.db.commit()
                return "Registro eliminado"
            else:
                return "No se encontró el registro"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def update(self, id, medical_license):
        existing_medical_license = self.db.query(MedicalLicenseModel).filter(MedicalLicenseModel.id == id).one_or_none()

        if not existing_medical_license:
            return "No se encontró el registro"

        existing_medical_license_data = medical_license.dict(exclude_unset=True)
        for key, value in existing_medical_license_data.items():
            setattr(existing_medical_license, key, value)

        self.db.commit()

        return "Registro actualizado"