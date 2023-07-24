from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.backend.db.database import get_db
from sqlalchemy.orm import Session
from app.backend.classes.authentication_class import AuthenticationClass
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta

login_users = APIRouter(
    prefix="/login_users",
    tags=["LoginUser"]
)

@login_users.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = AuthenticationClass(db).authenticate_user(form_data.username, form_data.password)
    access_token_expires = timedelta(minutes=30)
    access_token_jwt = AuthenticationClass(db).create_token({'sub': str(user.rut)}, access_token_expires)

    return {
        "access_token": access_token_jwt, 
        "rut": user.rut,
        "visual_rut": user.visual_rut,
        "rol_id": user.rol_id,
        "nickname": user.nickname,
        "token_type": "bearer"
    }

@login_users.post("/logout")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = AuthenticationClass(db).authenticate_user(form_data.username, form_data.password)
    access_token_expires = timedelta(minutes=30)
    access_token_jwt = AuthenticationClass(db).create_token({'sub': str(user.rut)}, access_token_expires)

    return {
        "access_token": access_token_jwt, 
        "rut": user.rut,
        "visual_rut": user.visual_rut,
        "rol_id": user.rol_id,
        "nickname": user.nickname,
        "token_type": "bearer"
    }