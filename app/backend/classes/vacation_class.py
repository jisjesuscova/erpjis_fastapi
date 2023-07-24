from app.backend.db.models import VacationModel, TotalVacationDaysModel
from app.backend.classes.employee_labor_datum_class import EmployeeLaborDatumClass
from app.backend.classes.employee_extra_datum_class import EmployeeExtraDatumClass
from app.backend.classes.helper_class import HelperClass
from datetime import date
from datetime import datetime

class VacationClass:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        try:
            data = self.db.query(VacationModel).order_by(VacationModel.id).all()
            if not data:
                return "No hay registros"
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def get(self, field, value):
        try:
            data = self.db.query(VacationModel).filter(getattr(VacationModel, field) == value).first()
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, vacation_inputs):
        days = HelperClass().days(vacation_inputs['since'], vacation_inputs['until'], vacation_inputs['no_valid_days'])

        vacation = VacationModel()
        vacation.document_employee_id = vacation_inputs['document_employee_id']
        vacation.rut = vacation_inputs['rut']
        vacation.since = vacation_inputs['since']
        vacation.until = vacation_inputs['until']
        vacation.days = days
        vacation.no_valid_days = vacation_inputs['no_valid_days']
        vacation.support = ''
        vacation.added_date = datetime.now()
        vacation.updated_date = datetime.now()

        self.db.add(vacation)
        try:
            self.db.commit()

            return 1
        except Exception as e:
            return 0
        
    def delete(self, id):
        try:
            data = self.db.query(VacationModel).filter(VacationModel.id == id).first()
            if data:
                self.db.delete(data)
                self.db.commit()
                return data.id
            else:
                return "No se encontró el registro"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def update(self, id, vacation):
        existing_vacation = self.db.query(VacationModel).filter(VacationModel.id == id).one_or_none()

        if not existing_vacation:
            return "No se encontró el registro"

        existing_vacation_data = vacation.dict(exclude_unset=True)
        for key, value in existing_vacation_data.items():
            setattr(existing_vacation, key, value)

        self.db.commit()

        return "Registro actualizado"
    
    def legal(self, rut):
        employee_labor_data = EmployeeLaborDatumClass(self.db).get("rut", rut)
        employee_extra_data = EmployeeExtraDatumClass(self.db).get("rut", rut)
        months = HelperClass(self.db).months(employee_labor_data.entrance_company, date.today())
        vacation_days = HelperClass(self.db).vacation_days(months, employee_extra_data.extreme_zone_id)

        return vacation_days
    
    def calculate_total_vacation_days(self):
        total_vacation_days = self.db.query(TotalVacationDaysModel).filter(TotalVacationDaysModel.id == 1).first()

        total = total_vacation_days.total_employee_vacation_days - (total_vacation_days.total_days - total_vacation_days.total_no_valid_days)

        return total
    