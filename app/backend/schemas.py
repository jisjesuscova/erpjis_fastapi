from pydantic import BaseModel
from fastapi import UploadFile
from typing import Union
from datetime import datetime

class BranchOffice(BaseModel):
    branch_office: str
    address: str
    region_id: int
    commune_id: int
    segment_id: int
    zone_id: int
    principal_id: int
    status_id: int
    visibility_id: int
    opening_date: str
    dte_code: int
    added_date: datetime
    updated_date: Union[datetime, None]

class Employee(BaseModel):
    rut: str
    names: str
    father_lastname: str
    mother_lastname: str
    gender_id: int
    nationality_id: int
    personal_email: str
    cellphone: str
    born_date: str
    privilege: Union[int, None]
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateBranchOffice(BaseModel):
    branch_office: str = None
    address: str = None
    region_id: int = None
    commune_id: int = None
    segment_id: int = None
    zone_id: int = None
    principal_id: int = None
    status_id: int = None
    visibility_id: int = None
    opening_date: str = None
    dte_code: int = None
    updated_date: Union[datetime, None]

class Gender(BaseModel):
    gender: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateGender(BaseModel):
    gender: str = None
    updated_date: Union[datetime, None]

class Nationality(BaseModel):
    nationality: str
    previred_code: int
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateNationality(BaseModel):
    nationality: str = None
    previred_code: int = None
    updated_date: Union[datetime, None]

class Pention(BaseModel):
    pention: str
    pention_remuneration_code: int
    rut: str
    amount: str
    previred_code: int
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdatePention(BaseModel):
    pention: str = None
    pention_remuneration_code: int = None
    rut: str = None
    amount: str = None
    previred_code: int = None
    updated_date: str = None

class Bank(BaseModel):
    visibility_id: int
    bank: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateBank(BaseModel):
    visibility_id: int = None
    bank: str = None
    updated_date: str = None

class Segment(BaseModel):
    segment: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateSegment(BaseModel):
    segment: str = None
    updated_date: Union[datetime, None]

class AccountType(BaseModel):
    id: int
    account_type: str
    added_date: str
    updated_date: str

class UpdateAccountType(BaseModel):
    account_type: str = None
    updated_date: str = None

class Region(BaseModel):
    id: int
    region: str
    region_remuneration_code: int
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateRegion(BaseModel):
    id: int = None
    region: str = None
    region_remuneration_code: int = None
    updated_date: Union[datetime, None]
    
class UpdateEmployee(BaseModel):
    rut: str = None
    names: str = None
    father_lastname: str = None
    mother_lastname: str = None
    gender_id: str = None
    nationality_id: str = None
    personal_email: str = None
    cellphone: str = None
    born_date: str = None
    privilege: int = None
    updated_date: Union[datetime, None]

class UserLogin(BaseModel):
    rol_id: Union[int, None]
    clock_rol_id: Union[int, None]
    status_id: Union[int, None]
    rut: Union[int, None]
    visual_rut: Union[str, None]
    nickname: Union[str, None]
    hashed_password: Union[str, None]
    disabled: Union[int, None]

class User(BaseModel):
    rol_id: int
    clock_rol_id: int
    status_id: int
    rut: str
    names: str
    father_lastname: str
    password: str
    disabled: int
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateUser(BaseModel):
    rol_id: int = None
    clock_rol_id: int = None
    status_id: int = None
    rut: str = None
    names: str = None
    father_lastname: str = None
    password: str = None
    updated_date: Union[datetime, None]

class Uniform(BaseModel):
    uniform_type_id: int
    rut: int
    delivered_date: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateUniform(BaseModel):
    uniform_type_id: int = None
    rut: int = None
    delivered_date: str = None
    updated_date: Union[datetime, None]

class EmployeeLaborDatum(BaseModel):
    rut: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateEmployeeLaborDatum(BaseModel):
    rut: str = None
    contract_type_id: int = None
    branch_office_id: int = None
    address: str = None
    region_id: int = None
    commune_id: int = None
    civil_state_id: int = None
    health_id: int = None
    pention_id: int = None
    job_position_id: int = None
    extreme_zone_id: int = None
    employee_type_id: int = None
    regime_id: int = None
    status_id: int = None
    health_payment_id: int = None
    entrance_pention: str = None
    entrance_company: str = None
    entrance_health: str = None
    salary: int = None
    collation: int = None
    locomotion: int = None
    extra_health_amount: str = None
    apv_payment_type_id: int = None
    apv_amount: str = None
    updated_date: Union[datetime, None]

class EmployeeExtra(BaseModel):
    rut: int
    updated_date: Union[datetime, None]

class UpdateEmployeeExtra(BaseModel):
    extreme_zone_id: int = None
    employee_type_id: int = None
    young_job_status_id: int = None
    be_paid_id: int = None
    suplemental_health_insurance_id: int = None
    pensioner_id: int = None
    disability_id: int = None
    suplemental_health_insurance_id: int = None
    progressive_vacation_level_id: int = None
    recognized_years: int = None
    progressive_vacation_status_id: int = None
    progressive_vacation_date: str = None
    updated_date: Union[datetime, None]

class AlertType(BaseModel):
    alert_type: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateAlertType(BaseModel):
    alert_type: str = None
    updated_date: Union[datetime, None]

class Honorary(BaseModel):
    id: int
    reason_id: int
    branch_office_id: int
    foreigner_id: int
    bank_id: int
    schedule_id: int
    region_id: int
    commune_id: int
    requested_by: int
    status_id: int
    accountability_status_id: int
    employee_to_replace: int
    rut: int
    full_name: str
    email: str
    address: str
    account_number: str
    start_date: str
    end_date: str
    amount: int
    observation: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateHonorary(BaseModel):
    reason_id: int = None
    branch_office_id: int = None
    foreigner_id: int = None
    bank_id: int = None
    schedule_id: int = None
    region_id: int = None
    commune_id: int = None
    requested_by: int = None
    status_id: int = None
    accountability_status_id: int = None
    employee_to_replace: int = None
    rut: int = None
    full_name: str = None
    email: str = None
    address: str = None
    account_number: str = None
    start_date: str = None
    end_date: str = None
    amount: int = None
    observation: str = None
    updated_date: Union[datetime, None]

class UniformType(BaseModel):
    uniform_type: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateUniformType(BaseModel):
    uniform_type: str = None
    updated_date: Union[datetime, None]

class JobPosition(BaseModel):
    job_position: str
    functions: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateJobPosition(BaseModel):
    job_position: str = None
    functions: str = None
    updated_date: Union[datetime, None]

class PatologyType(BaseModel):
    patology_type: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdatePatologyType(BaseModel):
    patology_type: str = None
    updated_date: Union[datetime, None]

class CivilState(BaseModel):
    civil_state: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateCivilState(BaseModel):
    civil_state: str = None
    updated_date: Union[datetime, None]

class DocumentType(BaseModel):
    document_type: str
    document_group_id: int
    order: int
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateDocumentType(BaseModel):
    document_type: str = None
    document_group_id: int = None
    order: int = None
    updated_date: Union[datetime, None]

class FamilyType(BaseModel):
    id: int
    family_type: str
    added_date: str
    updated_date: str

class UpdateFamilyType(BaseModel):
    family_type: str
    updated_date: str = None

class FamilyCoreDatum(BaseModel):
    id: int
    family_type_id: int
    rut_user: int
    gender_id: int
    rut: int
    names: str
    father_lastname: str
    mother_lastname: str
    born_date: str
    support: str
    added_date: str
    updated_date: str

class UpdateFamilyCoreDatum(BaseModel):
    family_type_id: int
    rut_user: int
    gender_id: int
    rut: int
    names: str
    father_lastname: str
    mother_lastname: str
    born_date: str
    support: str
    updated_date: str = None

class Vacation(BaseModel):
    id: int
    document_employee_id: int
    rut: int
    since: str
    until: str
    no_valid_days: int
    status_id: int
    document_type_id: int
    added_date: str
    updated_date: str

class UpdateVacation(BaseModel):
    document_employee_id: int = None
    rut: int = None
    since: str = None
    until: str = None
    days: int = None
    no_valid_days: int = None
    support: str = None
    updated_date: str = None

class MedicalLicense(BaseModel):
    id: int
    document_employee_id: int
    medical_license_type_id: int
    patology_type_id: int
    period: str
    rut: int
    folio: int
    since: str
    until: str
    days: int
    added_date: str
    updated_date: str

class UpdateMedicalLicense(BaseModel):
    document_employee_id: int = None
    medical_license_type_id: int = None
    patology_type_id: int = None
    period: str = None
    rut: int = None
    folio: int = None
    since: str = None
    until: str = None
    days: int = None
    updated_date: str = None

class Rol(BaseModel):
    rol: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateRol(BaseModel):
    rol: str = None
    updated_date: Union[datetime, None]

class HealthModel(BaseModel):
    id: int
    health_remuneration_code: int
    health: str
    rut: int
    previred_code: int
    added_date: str
    updated_date: str

class UpdateHealthModel(BaseModel):
    health_remuneration_code: int = None
    health: str = None
    rut: int = None
    previred_code: int = None
    updated_date: Union [datetime, None]

class New(BaseModel):
    title: str
    description: str
    markdown_description: str
    picture: UploadFile
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateNew(BaseModel):
    title: str = None
    description: str = None
    markdown_description: str = None
    picture: str = None
    updated_date: str = None

class Principal(BaseModel):
    id: int
    principal: str
    added_date: str
    updated_date: str

class UpdatePrincipal(BaseModel):
    principal: str = None
    updated_date: str = None

class Commune(BaseModel):
    region_id: int
    commune: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateCommune(BaseModel):
    region_id: int = None
    commune: str = None
    updated_date: Union[datetime, None]

class Health(BaseModel):
    health_remuneration_code: int
    health: str
    rut: int
    previred_code: int
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateHealth(BaseModel):
    health_remuneration_code: int = None
    health: str = None
    rut: int = None
    previred_code: int = None
    updated_date: Union[datetime, None]

class EmployeeBankAccount(BaseModel):
    id: int
    bank_id: int
    account_type_id: int
    status_id: int
    rut: int
    account_number: str
    added_date: str
    updated_date: str

class UpdateEmployeeBankAccount(BaseModel):
    bank_id: int = None
    account_type_id: int = None
    status_id: int = None
    rut: int = None
    account_number: str = None
    updated_date: str = None

class DocumentEmployee(BaseModel):
    id: int
    status_id: int
    document_type_id: int
    old_document_status_id: int
    rut: int
    added_date: str
    updated_date: str

class UpdateDocumentEmployee(BaseModel):
    status_id: int = None
    document_type_id: int = None
    old_document_status_id: int = None
    rut: int = None
    support: str = None
    updated_date: str = None

class UploadDocumentEmployee(BaseModel):
    id: int
    rut: int
    file_name: str
    dropbox_path: str
    support: UploadFile
    updated_date: str = None

class SearchEmployee(BaseModel):
    rut: Union[str, None]
    names: Union[str, None]
    father_lastname: Union[str, None]
    mother_lastname: Union[str, None]
    status_id: Union[int, None]
    branch_office_id: Union[int, None]
    cellphone: Union[str, None]

class ClockUser(BaseModel):
    rut: str
    names: str
    father_lastname: str
    privilege: str
    added_date: Union[str, None]
    updated_date: Union[str, None]

class UpdateClockUser(BaseModel):
    rut: str = None
    names: str = None
    father_lastname: str = None
    privilege: str = None
    updated_date: Union[str, None]

class ContractDatum(BaseModel):
    rut: int
    status_id: int
    document_type_id: int

class ContractType(BaseModel):
    contract_type: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateContractType(BaseModel):
    contract_type: str = None
    updated_date: Union[datetime, None]

class MedicalLicenseType(BaseModel):
    medical_license_type: str
    added_date: datetime
    updated_date: Union[datetime, None]

class UpdateMedicalLicenseType(BaseModel):
    medical_license_type: str = None
    updated_date: Union[datetime, None]