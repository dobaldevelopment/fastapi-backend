from app.models.db import Base, engine
from app.models import usuario_model

Base.metadata.create_all(bind=engine)
