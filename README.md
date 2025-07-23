# 🔐 Backend API con FastAPI

Este proyecto es un backend RESTful hecho con FastAPI, que incluye autenticación JWT, persistencia de datos con SQLite y SQLAlchemy, y un CRUD completo para Posts.

## ❓ Motivación del proyecto

Mi objetivo fue consolidar conocimientos en **Python**, **FastAPI**, y autenticación segura con **JWT**, además de aplicar herramientas que uso frecuentemente como **Docker**, **GitHub Actions** y despliegue en la nube.

Este repo nace como parte de mi proceso de aprendizaje en desarrollo backend, automatización y ciberseguridad. Construí algo funcional pero también escalable — una base que me sirva como punto de partida para proyectos más complejos.

## ⚙️ Características

- Registro y login de usuarios
- Hashing de contraseñas seguro con Bcrypt
- Generación y validación de tokens JWT
- Rutas protegidas
- CRUD de posts persistente
- Estructura modular
- SQLite como base de datos local
- Listo para escalar a PostgreSQL y Docker

## 🧠 Tecnologías utilizadas

- **FastAPI**: Framework moderno para construir APIs rápidas y bien documentadas
- **JWT**: Para proteger rutas mediante tokens seguros
- **SQLAlchemy** + **PostgreSQL**: ORM y base de datos relacional
- **Docker**: Contenedores para reproducibilidad
- **Docker Compose**: Orquestación del entorno local
- **GitHub Actions**: Pipeline de pruebas, linting y deploy automático
- **Swagger / OpenAPI**: Documentación auto-generada
- **Pytest**: Pruebas unitarias e integración (en progreso)

## 📦 Estructura del proyecto

📁 app  
│ ├── 📁 api  
│ │ ├── routes  
│ │ ├── models  
│ │ └── schemas  
│ ├── 📁 core  
│ │ ├── config  
│ │ └── security  
│ ├── 📁 db  
│ │ └── database_setup  
│  
📁 tests  
│ └── unit_integration  
│  
📄 Dockerfile  
📄 docker-compose.yml  
📄 requirements.txt  
📄 README.md

## ℹ️ Cómo usar

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


## 🧪 Pruebas

En progreso: estamos integrando `Pytest` para validar endpoints, tokens y comportamiento de errores. También se agregará exportación de reportes de cobertura.

## ✍️ Notas personales

Durante este proyecto aprendí a configurar JWT a fondo, manejar variables de entorno de forma segura, y automatizar pipelines con GitHub Actions. Tardé un poco en adaptar el Dockerfile para producción, pero ahora funciona como base para cualquier backend FastAPI que quiera escalar.

Algunas ideas para próximos pasos:
- Agregar roles y permisos
- Exportar la documentación como PDF
- Subir colección Postman para testing manual

## 📎 Links útiles

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [JWT Intro](https://jwt.io/introduction)
- [Docker Best Practices](https://docs.docker.com/develop/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

## 📣 Contacto

🧑‍💻 Autor: **Adriel Dobal**  
📧 Email: dobaladri5@gmail.com  
🌐 GitHub: [Dobaldevelopment](https://github.com/dobaldevelopment)  
🔗 LinkedIn: [Adriel Dobal]([https://www.linkedin.com/in/adriel-dobal](https://www.linkedin.com/in/adriel-a-j-dobal-%F0%9F%87%A6%F0%9F%87%B7-%F0%9F%87%BA%F0%9F%87%B8-93799b259/)

---
