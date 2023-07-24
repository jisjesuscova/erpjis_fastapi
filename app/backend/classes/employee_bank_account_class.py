from app.backend.db.models import EmployeeBankAccountModel

class EmployeeBankAccountClass:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        try:
            data = self.db.query(EmployeeBankAccountModel).order_by(EmployeeBankAccountModel.id).all()
            if not data:
                return "No data found"
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def get(self, field, value):
        try:
            data = self.db.query(EmployeeBankAccountModel).filter(getattr(EmployeeBankAccountModel, field) == value).first()
            return data
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
    
    def store(self, EmployeeBankAccount_inputs):
        try:
            data = EmployeeBankAccountModel(**EmployeeBankAccount_inputs)
            self.db.add(data)
            self.db.commit()
            return 1
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def delete(self, id):
        try:
            data = self.db.query(EmployeeBankAccountModel).filter(EmployeeBankAccountModel.id == id).first()
            if data:
                self.db.delete(data)
                self.db.commit()
                return 1
            else:
                return "No data found"
        except Exception as e:
            error_message = str(e)
            return f"Error: {error_message}"
        
    def update(self, id, employee_bank_account):
        existing_employee_bank_account = self.db.query(EmployeeBankAccountModel).filter(EmployeeBankAccountModel.id == id).one_or_none()

        if not existing_employee_bank_account:
            return "No data found"

        existing_employee_bank_account_data = employee_bank_account.dict(exclude_unset=True)
        for key, value in existing_employee_bank_account_data.items():
            setattr(existing_employee_bank_account, key, value)

        self.db.commit()

        return 1