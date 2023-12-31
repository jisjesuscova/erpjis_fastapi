from app.backend.db.database import Base_one, Base_two
from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, Float, Boolean, Text

class BranchOfficeModel(Base_one):
    __tablename__ = 'branch_offices'

    id = Column(Integer, primary_key=True)
    branch_office = Column(String(255))
    address = Column(String(255))
    region_id = Column(Integer, ForeignKey('regions.id'))
    commune_id = Column(Integer, ForeignKey('communes.id'))
    segment_id = Column(Integer, ForeignKey('segments.id'))
    zone_id = Column(Integer, ForeignKey('zones.id'))
    principal_id = Column(Integer, ForeignKey('principals.id'))
    status_id = Column(Integer)
    visibility_id = Column(Integer)
    opening_date = Column(Integer)
    dte_code = Column(Integer)
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class GenderModel(Base_one):
    __tablename__ = 'genders'

    id = Column(Integer, primary_key=True)
    gender = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class NationalityModel(Base_one):
    __tablename__ = 'nationalities'

    id = Column(Integer, primary_key=True)
    nationality = Column(String(255))
    previred_code = Column(Integer)
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class PentionModel(Base_one):
    __tablename__ = 'pentions'

    id = Column(Integer, primary_key=True)
    pention = Column(String(255))
    pention_remuneration_code = Column(Integer)
    rut = Column(String(255))
    amount = Column(String(255))
    previred_code = Column(Integer)
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class BankModel(Base_one):
    __tablename__ = 'banks'

    id = Column(Integer, primary_key=True)
    visibility_id = Column(Integer)
    bank = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class AccountTypeModel(Base_one):
    __tablename__ = 'account_types'

    id = Column(Integer, primary_key=True)
    account_type = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class SupervisorModel(Base_one):
    __tablename__ = 'supervisors'

    id = Column(Integer, primary_key=True)
    branch_office_id = Column(Integer, ForeignKey('branch_offices.id'))
    rut = Column(Integer)
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class NewModel(Base_one):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text())
    markdown_description = Column(Text())
    picture = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class RegionModel(Base_one):
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    region = Column(String(255))    
    region_remuneration_code = Column(Integer) 
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class TotalVacationDaysModel(Base_one):
    __tablename__ = 'total_vacation_days'

    id = Column(Integer, primary_key=True)
    total_days = Column(Integer)
    total_no_valid_days = Column(Integer)
    total_employee_vacation_days = Column(Integer)

class EmployeeModel(Base_one):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    rut = Column(Integer)
    visual_rut = Column(String(20))
    names = Column(String(255))
    father_lastname = Column(String(255))
    mother_lastname = Column(String(255))
    gender_id = Column(Integer)
    nationality_id = Column(Integer)
    personal_email = Column(String(255))
    cellphone = Column(String(100))
    born_date = Column(Date())
    picture = Column(String(255))
    signature = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class UserModel(Base_one):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    rol_id = Column(Integer, ForeignKey('rols.id'))
    clock_rol_id = Column(Integer)
    status_id = Column(Integer)
    rut = Column(Integer)
    visual_rut = Column(String(20))
    nickname = Column(String(255))
    hashed_password = Column(String(255))
    disabled = Column(Integer)
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class ContractTypeModel(Base_one):
    __tablename__ = 'contract_type'

    id = Column(Integer, primary_key=True)
    contract_type = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class CivilStateModel(Base_one):
    __tablename__ = 'civil_states'

    id = Column(Integer, primary_key=True)
    civil_state = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class UniformModel(Base_one):
    __tablename__ = 'uniforms'

    id = Column(Integer, primary_key=True)
    uniform_type_id = Column(Integer, ForeignKey('uniform_types.id'))
    rut = Column(Integer)
    delivered_date = Column(Date())
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class EmployeeTypeModel(Base_one):
    __tablename__ = 'employee_types'

    id = Column(Integer, primary_key=True)
    employee_type = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class EmployeeLaborDatumModel(Base_one):
    __tablename__ = 'employee_labor_data'

    id = Column(Integer, primary_key=True)
    rut = Column(Integer)
    visual_rut = Column(String(20))
    contract_type_id = Column(Integer, ForeignKey('contract_type.id'))
    branch_office_id = Column(Integer, ForeignKey('branch_offices.id'))
    address = Column(String(255))
    region_id = Column(Integer, ForeignKey('regions.id'))
    commune_id = Column(Integer, ForeignKey('communes.id'))
    civil_state_id = Column(Integer, ForeignKey('civil_states.id'))
    health_id = Column(Integer, ForeignKey('healths.id'))
    pention_id = Column(Integer, ForeignKey('pentions.id'))
    job_position_id = Column(Integer, ForeignKey('job_positions.id'))
    extreme_zone_id = Column(Integer)
    employee_type_id = Column(Integer, ForeignKey('employee_types.id'))
    regime_id = Column(Integer, ForeignKey('regimes.id'))
    status_id = Column(Integer)
    health_payment_id = Column(Integer)
    entrance_pention  = Column(Date())
    entrance_company  = Column(Date())
    entrance_health = Column(Date())
    exit_company  = Column(Date())
    salary = Column(Integer)
    collation = Column(Integer)
    locomotion = Column(Integer)
    extra_health_amount = Column(String(255))
    apv_payment_type_id = Column(Integer)
    apv_amount = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class EmployeeExtraModel(Base_one):
    __tablename__ = 'employee_extras'

    id = Column(Integer, primary_key=True)
    rut = Column(Integer)
    visual_rut = Column(String(20))
    extreme_zone_id = Column(Integer)
    employee_type_id = Column(Integer, ForeignKey('employee_types.id'))
    young_job_status_id = Column(Integer)
    be_paid_id = Column(Integer)
    suplemental_health_insurance_id = Column(Integer)
    pensioner_id = Column(Integer)
    disability_id = Column(Integer)
    suplemental_health_insurance_id = Column(Integer)
    progressive_vacation_level_id = Column(Integer)
    recognized_years = Column(Integer)
    progressive_vacation_status_id = Column(Integer)
    progressive_vacation_date = Column(Date())
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class RegimeModel(Base_one):
    __tablename__ = 'regimes'

    id = Column(Integer, primary_key=True)
    regime = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class EmployeeViewModel(Base_one):
    __tablename__ = 'employee_details'
    __table_args__ = {'info': {'is_view': True}}  # Indica que es una vista

    id = Column(Integer, primary_key=True)
    rol_id = Column(Integer, ForeignKey('rols.id'))
    clock_rol_id = Column(Integer)
    status_id = Column(Integer)
    rut = Column(Integer)
    visual_rut = Column(String(20))
    nickname = Column(String(255))
    names = Column(String(255))
    father_lastname = Column(String(255))
    mother_lastname = Column(String(255))
    nickname = Column(String(255))
    gender_id = Column(Integer)
    nationality_id = Column(Integer)
    personal_email = Column(String(255))
    cellphone = Column(String(100))
    born_date = Column(Date())
    picture = Column(String(255))
    signature = Column(String(255))
    contract_type_id = Column(Integer, ForeignKey('contract_types.id'))
    branch_office_id = Column(Integer, ForeignKey('branch_offices.id'))
    address = Column(String(255))
    region_id = Column(Integer, ForeignKey('regions.id'))
    commune_id = Column(Integer, ForeignKey('communes.id'))
    civil_state_id = Column(Integer, ForeignKey('civil_states.id'))
    health_id = Column(Integer, ForeignKey('healths.id'))
    pention_id = Column(Integer, ForeignKey('pentions.id'))
    job_position_id = Column(Integer, ForeignKey('job_positions.id'))
    extreme_zone_id = Column(Integer, ForeignKey('extreme_zones.id'))
    employee_type_id = Column(Integer, ForeignKey('employee_types.id'))
    regime_id = Column(Integer, ForeignKey('regimes.id'))
    status_id = Column(Integer)
    health_payment_id = Column(Integer, ForeignKey('health_payments.id'))
    entrance_pention  = Column(Date())
    entrance_company  = Column(Date())
    entrance_health = Column(Date())
    exit_company  = Column(Date())
    salary = Column(Integer)
    collation = Column(Integer)
    locomotion = Column(Integer)
    company_email = Column(String(255))
    extra_health_amount = Column(String(255))
    apv_payment_type_id = Column(Integer, ForeignKey('apv_payment_types.id'))
    apv_amount = Column(String(255))
    young_job_status_id = Column(Integer)
    be_paid_id = Column(Integer)
    suplemental_health_insurance_id = Column(Integer)
    pensioner_id = Column(Integer)
    disability_id = Column(Integer)
    suplemental_health_insurance_id = Column(Integer)
    progressive_vacation_level_id = Column(Integer)
    recognized_years = Column(Integer)
    progressive_vacation_status_id = Column(Integer)
    progressive_vacation_date = Column(Date())
    progressive_vacation_level_id = Column(Integer)

class AlertTypeModel(Base_one):
    __tablename__ = 'alert_types'

    id = Column(Integer, primary_key=True)
    alert_type = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class HonoraryModel(Base_one):
    __tablename__ = 'honoraries'

    id = Column(Integer, primary_key=True)
    reason_id = Column(Integer)
    branch_office_id = Column(Integer, ForeignKey('branch_offices.id'))
    foreigner_id = Column(Integer)
    bank_id = Column(Integer, ForeignKey('banks.id'))
    schedule_id = Column(Integer)
    region_id = Column(Integer, ForeignKey('regions.id'))
    commune_id = Column(Integer, ForeignKey('communes.id'))
    requested_by = Column(Integer)
    status_id = Column(Integer)
    accountability_status_id = Column(Integer)
    employee_to_replace = Column(Integer)
    rut = Column(Integer)
    full_name = Column(String(255))
    email = Column(String(255))
    address = Column(String(255))
    account_number = Column(String(255))
    start_date = Column(Date())
    end_date = Column(Date())
    amount = Column(Integer)
    observation = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class UniformTypeModel(Base_one):
    __tablename__ = 'uniform_types'

    id = Column(Integer, primary_key=True)
    uniform_type = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class SegmentModel(Base_one):
    __tablename__ = 'segments'

    id = Column(Integer, primary_key=True)
    segment = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class JobPositionModel(Base_one):
    __tablename__ = 'job_positions'

    id = Column(Integer, primary_key=True)
    job_position = Column(String(255))
    functions = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class PatologyTypeModel(Base_one):
    __tablename__ = 'patology_types'

    id = Column(Integer, primary_key=True)
    patology_type = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class DocumentTypeModel(Base_one):
    __tablename__ = 'document_types'

    id = Column(Integer, primary_key=True)
    document_type = Column(String(255))
    document_group_id = Column(Integer) 
    order = Column(Integer) 
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class FamilyTypeModel(Base_one):
    __tablename__ = 'family_types'

    id = Column(Integer, primary_key=True)
    family_type = Column(String(255))
    added_date = Column(DateTime())

class FamilyCoreDatumModel(Base_one):
    __tablename__ = 'family_core_data'

    id = Column(Integer, primary_key=True)
    family_type_id = Column(Integer, ForeignKey('family_types.id'))
    rut_user = Column(Integer)
    gender_id = Column(Integer, ForeignKey('genders.id'))
    rut = Column(Integer)
    names = Column(String(255))
    father_lastname = Column(String(255))
    mother_lastname = Column(String(255))
    born_date = Column(DateTime())
    support = Column(Text)
    added_date = Column(DateTime())

class VacationModel(Base_one):
    __tablename__ = 'vacations'

    id = Column(Integer, primary_key=True)
    document_employee_id = Column(Integer)
    rut = Column(Integer)
    since = Column(Date())
    until = Column(Date())
    days = Column(Integer)
    no_valid_days = Column(Integer)
    support = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class MedicalLicenseModel(Base_one):
    __tablename__ = 'medical_licenses'

    id = Column(Integer, primary_key=True)
    document_employee_id = Column(Integer)
    medical_license_type_id = Column(Integer, ForeignKey('medical_license_types.id'))
    patology_type_id = Column(Integer, ForeignKey('patology_types.id'))
    period = Column(String(255))
    rut = Column(Integer)
    folio = Column(String(255))
    since = Column(Date())
    until = Column(Date())
    days = Column(Integer)
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class RolModel(Base_one):
    __tablename__ = 'rols'

    id = Column(Integer, primary_key=True)
    rol = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class PrincipalModel(Base_one):
    __tablename__ = 'principals'

    id = Column(Integer, primary_key=True)
    principal = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class SettingModel(Base_one):
    __tablename__ = 'settings'

    id = Column(Integer, primary_key=True)
    dropbox_token = Column(Text)
    facebook_token = Column(Text)
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class CommuneModel(Base_one):
    __tablename__ = 'communes'

    id = Column(Integer, primary_key=True)
    region_id = Column(Integer, ForeignKey('regions.id'))
    commune = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class HealthModel(Base_one):
    __tablename__ = 'healths'

    id = Column(Integer, primary_key=True)
    health_remuneration_code = Column(Integer)
    health = Column(String(255))
    rut = Column(Integer)
    previred_code = Column(Integer)
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class EmployeeBankAccountModel(Base_one):
    __tablename__ = 'employees_bank_accounts'

    id = Column(Integer, primary_key=True)
    bank_id = Column(Integer, ForeignKey('banks.id'))
    account_type_id = Column(Integer)
    status_id = Column(Integer)
    rut = Column(Integer)
    account_number = Column(Integer)
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class DocumentEmployeeModel(Base_one):
    __tablename__ = 'documents_employees'

    id = Column(Integer, primary_key=True)
    status_id = Column(Integer)
    document_type_id = Column(Integer, ForeignKey('document_types.id'))
    old_document_status_id = Column(Integer)
    rut = Column(Integer)
    support = Column(String(255))
    added_date =  Column(DateTime())
    updated_date = Column(DateTime())

class OldEmployeeModel(Base_one):
    __tablename__ = 'old_employees'

    id = Column(Integer, primary_key=True)
    rut = Column(Integer)
    visual_rut = Column(String(20))
    names = Column(String(255))
    father_lastname = Column(String(255))
    mother_lastname = Column(String(255))
    nickname = Column(String(255))
    order_id = Column(Integer)
    gender_id = Column(Integer)
    nationality_id = Column(Integer)
    personal_email = Column(String(255))
    cellphone = Column(String(100))
    born_date = Column(Date())
    picture = Column(String(255))
    signature = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class OldEmployeeLaborDatumModel(Base_one):
    __tablename__ = 'old_employee_labor_data'

    id = Column(Integer, primary_key=True)
    rut = Column(Integer)
    visual_rut = Column(String(20))
    contract_type_id = Column(Integer, ForeignKey('contract_types.id'))
    branch_office_id = Column(Integer, ForeignKey('branch_offices.id'))
    address = Column(String(255))
    region_id = Column(Integer, ForeignKey('regions.id'))
    commune_id = Column(Integer, ForeignKey('communes.id'))
    civil_state_id = Column(Integer, ForeignKey('civil_states.id'))
    health_id = Column(Integer, ForeignKey('healths.id'))
    pention_id = Column(Integer, ForeignKey('pentions.id'))
    job_position_id = Column(Integer)
    employee_type_id = Column(Integer)
    regime_id = Column(Integer)
    order_id = Column(Integer)
    status_id = Column(Integer)
    health_payment_id = Column(Integer)
    entrance_pention  = Column(Date())
    entrance_company  = Column(Date())
    entrance_health = Column(Date())
    exit_company  = Column(Date())
    salary = Column(Integer)
    collation = Column(Integer)
    extra_health_amount = Column(String(255))
    locomotion = Column(Integer)
    company_email = Column(String(255))
    apv_payment_type_id = Column(Integer)
    apv_amount = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class ClockUserModel(Base_one):
    __tablename__ = 'clock_users'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer)
    rut = Column(Integer)
    full_name = Column(String(255))
    privilege = Column(Integer)
    added_date = Column(DateTime())
    updated_date = Column(DateTime())

class MedicalLicenseTypeModel(Base_one):
    __tablename__ = 'medical_license_types'

    id = Column(Integer, primary_key=True)
    medical_license_type = Column(String(255))
    added_date = Column(DateTime())
    updated_date = Column(DateTime())
