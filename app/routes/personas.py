from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.auth.jwt_bearer import JWTBearer

router = APIRouter()

class Persona(BaseModel):
    nombre: str
    edad: int

router.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"¡Hola, {nombre}!"}

