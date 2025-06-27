# Backend API con FastAPI 🚀

Este proyecto es un backend RESTful hecho con FastAPI, que incluye autenticación JWT, persistencia de datos con SQLite y SQLAlchemy, y un CRUD completo para Posts.

## Características

- Registro y login de usuarios
- Hashing de contraseñas seguro con Bcrypt
- Generación y validación de tokens JWT
- Rutas protegidas
- CRUD de posts persistente
- Estructura modular
- SQLite como base de datos local
- Listo para escalar a PostgreSQL y Docker

## Cómo usar

1. Clonar este repositorio  
2. Crear entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Ejecutar el servidor:

bash
uvicorn app.main:app --reload
Visitar la documentación automática en http://localhost:8000/docs

Tecnologías
FastAPI

Python

SQLAlchemy

JWT

Pydantic

Uvicorn

Passlib
