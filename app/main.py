from fastapi import FastAPI
from app.routes import personas, usuarios, posts

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "¡Hola desde tu backend FastAPI!"}

app.include_router(personas.router)
app.include_router(usuarios.router)
app.include_router(posts.router)

# Crear tablas
from app.models import usuario_model, post_model
from app.models.db import Base, engine
Base.metadata.create_all(bind=engine)


