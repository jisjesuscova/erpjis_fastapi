from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI_ONE = "mysql+pymysql://erpjisv1:Macana11@erpjisv1.mysql.database.azure.com:3306/erp_jis_v1"
engine_one = create_engine(SQLALCHEMY_DATABASE_URI_ONE)
SessionLocal_one = sessionmaker(bind=engine_one, autocommit=False, autoflush=False)
Base_one = declarative_base()

SQLALCHEMY_DATABASE_URI_TWO = "mysql+pymysql://erpjis@erpjis:Macana11@erpjis.mysql.database.azure.com:3306/erp_jis"
engine_two = create_engine(SQLALCHEMY_DATABASE_URI_TWO)
SessionLocal_two = sessionmaker(bind=engine_two, autocommit=False, autoflush=False)
Base_two = declarative_base()

def get_db():
    db = SessionLocal_one()
    try:
        yield db
    finally:
        db.close()

def get_db_two():
    db = SessionLocal_two()
    try:
        yield db
    finally:
        db.close()