from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.models.usuario_model import Usuario as UsuarioDB
from app.models.dependencias import get_db
from app.auth.jwt_handler import crear_token

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Usuario(BaseModel):
    username: str
    password: str

@router.post("/registro")
def registrar(usuario: Usuario, db: Session = Depends(get_db)):
    db_user = db.query(UsuarioDB).filter(UsuarioDB.username == usuario.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Usuario ya existe.")
    
    hashed_password = pwd_context.hash(usuario.password)
    nuevo_usuario = UsuarioDB(username=usuario.username, password=hashed_password)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return {"mensaje": "Usuario registrado correctamente."}

@router.post("/login")
def login(usuario: Usuario, db: Session = Depends(get_db)):
    db_user = db.query(UsuarioDB).filter(UsuarioDB.username == usuario.username).first()
    if not db_user or not pwd_context.verify(usuario.password, db_user.password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas.")
    
    token = crear_token({"sub": usuario.username})
    return {"access_token": token, "token_type": "bearer"}

