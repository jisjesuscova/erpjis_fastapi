from app.backend.db.models import EmployeeModel, EmployeeLaborDatumModel, BranchOfficeModel, OldEmployeeModel, OldEmployeeLaborDatumModel, SupervisorModel, EmployeeLaborDatumModel
from datetime import datetime
from sqlalchemy import func
from app.backend.classes.helper_class import HelperClass

class EmployeeClass:
    def __init__(self, db):
        self.db = db

    def get_all(self, rut = None, rol_id = None):
        try:
            if rol_id == 3:
                data = self.db.query(EmployeeModel, EmployeeLaborDatumModel, BranchOfficeModel, SupervisorModel). \
                    outerjoin(EmployeeLaborDatumModel, EmployeeLaborDatumModel.rut == EmployeeModel.rut). \
                    outerjoin(BranchOfficeModel, BranchOfficeModel.id == EmployeeLaborDatumModel.branch_office_id). \
                    outerjoin(SupervisorModel, SupervisorModel.branch_office_id == BranchOfficeModel.id). \
                    filter(SupervisorModel.rut == rut). \
                    order_by(EmployeeModel.names). \
                    all()
            else:
                data = self.db.query(EmployeeModel).order_by(EmployeeModel.id).all()

            if not data:
                return "No data found"
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def search(self, search_inputs):
        if len(search_inputs) > 0:
            search_rut = search_inputs['rut']
            search_names = search_inputs['names']
            search_father_lastname = search_inputs['father_lastname']
            search_mother_lastname = search_inputs['mother_lastname']
            search_status_id = search_inputs['status_id']
            search_branch_office_id = search_inputs['branch_office_id']
            search_cellphone = search_inputs['cellphone']
        
        if search_status_id == '2':
            query = self.db.query(OldEmployeeModel).join(OldEmployeeLaborDatumModel, OldEmployeeLaborDatumModel.rut == OldEmployeeModel.rut).add_columns(OldEmployeeModel.id, OldEmployeeModel.rut, OldEmployeeModel.visual_rut, OldEmployeeModel.nickname).order_by('rut')

            query = query.filter(OldEmployeeLaborDatumModel.status_id.like(f"%{search_status_id}%"))

            if len(search_inputs) > 0:
                if search_rut:
                    query = query.filter(OldEmployeeModel.visual_rut.like(f"%{search_rut}%"))
                if search_names:
                    query = query.filter(OldEmployeeModel.nickname.like(f"%{search_names}%"))
                if search_father_lastname:
                    query = query.filter(OldEmployeeModel.father_lastname.like(f"%{search_father_lastname}%"))
                if search_mother_lastname:
                    query = query.filter(OldEmployeeModel.mother_lastname.like(f"%{search_mother_lastname}%"))
                if search_branch_office_id:
                    query = query.filter(OldEmployeeLaborDatumModel.branch_office_id == search_branch_office_id)
            
            employees = query.all()
        elif search_status_id == '3':
            query = OldEmployeeModel.query\
                        .join(OldEmployeeLaborDatumModel, OldEmployeeLaborDatumModel.rut == OldEmployeeModel.rut)\
                        .add_columns(OldEmployeeModel.id, OldEmployeeModel.rut, OldEmployeeModel.visual_rut, OldEmployeeModel.nickname, OldEmployeeModel.names, OldEmployeeModel.father_lastname, OldEmployeeModel.mother_lastname).order_by('rut')

            query = query.filter(OldEmployeeLaborDatumModel.status_id.like(f"%{search_status_id}%"))

            if len(search_inputs) > 0:
                if search_rut:
                    query = query.filter(OldEmployeeModel.visual_rut.like(f"%{search_rut}%"))
                if search_names:
                    query = query.filter(OldEmployeeModel.names.like(f"%{search_names}%"))
                if search_father_lastname:
                    query = query.filter(OldEmployeeModel.father_lastname.like(f"%{search_father_lastname}%"))
                if search_mother_lastname:
                    query = query.filter(OldEmployeeModel.mother_lastname.like(f"%{search_mother_lastname}%"))
                if search_branch_office_id:
                    query = query.filter(OldEmployeeLaborDatumModel.branch_office_id == search_branch_office_id)
            
            employees = query.all()
        else:
            query = self.db.query(EmployeeModel).join(EmployeeLaborDatumModel, EmployeeLaborDatumModel.rut == EmployeeModel.rut).add_columns(EmployeeModel.id, EmployeeModel.rut, EmployeeModel.visual_rut, EmployeeModel.names, EmployeeModel.father_lastname, EmployeeModel.mother_lastname).order_by('rut')

            if len(search_inputs) > 0:
                if search_rut:
                    query = query.filter(EmployeeModel.visual_rut.like(f"%{search_rut}%"))
                if search_names:
                    query = query.filter(EmployeeModel.names.like(f"%{search_names}%"))
                if search_father_lastname:
                    query = query.filter(EmployeeModel.father_lastname.like(f"%{search_father_lastname}%"))
                if search_mother_lastname:
                    query = query.filter(EmployeeModel.mother_lastname.like(f"%{search_mother_lastname}%"))
                if search_branch_office_id:
                    query = query.filter(EmployeeLaborDatumModel.branch_office_id == search_branch_office_id)
                if search_cellphone:
                    query = query.filter(EmployeeModel.cellphone == search_cellphone)

            employees = query.all()

        return employees
        
    def get(self, field, value):
        try:
            data = self.db.query(EmployeeModel).filter(getattr(EmployeeModel, field) == value).first()
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, employee_inputs):
        numeric_rut = HelperClass().numeric_rut(str(employee_inputs['rut']))

        employee = EmployeeModel()
        employee.rut = numeric_rut
        employee.visual_rut = employee_inputs['rut']
        employee.names = employee_inputs['names']
        employee.father_lastname = employee_inputs['father_lastname']
        employee.mother_lastname = employee_inputs['mother_lastname']
        employee.gender_id = employee_inputs['gender_id']
        employee.nationality_id = employee_inputs['nationality_id']
        employee.personal_email = employee_inputs['personal_email']
        employee.cellphone = employee_inputs['cellphone']
        employee.born_date = employee_inputs['born_date']
        employee.added_date = datetime.now()

        self.db.add(employee)

        try:
            self.db.commit()

            return 1
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def delete(self, id):
        try:
            data = self.db.query(EmployeeModel).filter(EmployeeModel.rut == id).first()
            if data:
                self.db.delete(data)
                self.db.commit()
                return 1
            else:
                return "No data found"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def update(self, id, employee_inputs):
        employee =  self.db.query(EmployeeModel).filter(EmployeeModel.rut == id).one_or_none()

        if employee_inputs['rut'] != None:
            numeric_rut = HelperClass().numeric_rut(str(employee_inputs['rut']))
            employee.rut = numeric_rut
            employee.visual_rut = employee_inputs['rut']
        
        if employee_inputs['names'] != None:
            employee.names = employee_inputs['names']
        
        if employee_inputs['father_lastname'] != None:
            employee.father_lastname = employee_inputs['father_lastname']
        
        if employee_inputs['mother_lastname'] != None:
            employee.mother_lastname = employee_inputs['mother_lastname']

        if employee_inputs['gender_id'] != None:
            employee.gender_id = employee_inputs['gender_id']

        if employee_inputs['nationality_id'] != None:
            employee.nationality_id = employee_inputs['nationality_id']
        
        if employee_inputs['personal_email'] != None:
            employee.personal_email = employee_inputs['personal_email']
        
        if employee_inputs['cellphone'] != None:
            employee.cellphone = employee_inputs['cellphone']
        
        if employee_inputs['born_date'] != None:
            employee.born_date = employee_inputs['born_date']

        employee.update_date = datetime.now()

        self.db.add(employee)

        try:
            self.db.commit()

            return 1
        except Exception as e:
            return 0
    
    def get_birthdays(self):
        today = datetime.today()

        employees = self.db.query(
            EmployeeModel.rut,
            EmployeeModel.names,
            EmployeeModel.father_lastname,
            BranchOfficeModel.branch_office,
            func.DATE_FORMAT(EmployeeModel.born_date, "%d").label('day'),
            func.DATE_FORMAT(EmployeeModel.born_date, "%M").label('month')
        ) \
        .join(EmployeeLaborDatumModel, EmployeeLaborDatumModel.rut == EmployeeModel.rut) \
        .join(BranchOfficeModel, BranchOfficeModel.id == EmployeeLaborDatumModel.branch_office_id) \
        .filter(func.DAY(EmployeeModel.born_date) >= today.day, func.MONTH(EmployeeModel.born_date) == today.month) \
        .order_by(func.DAY(EmployeeModel.born_date)) \
        .limit(4) \
        .all()

        return employees
    
    def gender_totals(self):
        men_total = self.db.query(EmployeeModel).filter(EmployeeModel.gender_id == 1).count()
        women_total = self.db.query(EmployeeModel).filter(EmployeeModel.gender_id == 2).count()

        totals = [
            {'gender': 'Men', 'total': men_total},
            {'gender': 'Women', 'total': women_total}
        ]
    
        return totals
    
    def validate_cellphone(self, cellphone):
        existence = self.db.query(EmployeeModel).filter(EmployeeModel.cellphone == cellphone).count()

        if existence == 1:
            return 1
        else:
            return 0