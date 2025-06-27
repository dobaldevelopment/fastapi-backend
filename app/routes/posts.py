from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.models.dependencias import get_db
from app.models.post_model import Post as PostDB
from app.auth.jwt_bearer import JWTBearer

router = APIRouter()

class Post(BaseModel):
    titulo: str
    contenido: str

@router.post("/posts", dependencies=[Depends(JWTBearer())])
def crear_post(post: Post, db: Session = Depends(get_db)):
    nuevo = PostDB(**post.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/posts", dependencies=[Depends(JWTBearer())])
def obtener_posts(db: Session = Depends(get_db)):
    return db.query(PostDB).all()

@router.get("/posts/{post_id}", dependencies=[Depends(JWTBearer())])
def obtener_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(PostDB).filter(PostDB.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    return post

@router.delete("/posts/{post_id}", dependencies=[Depends(JWTBearer())])
def eliminar_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(PostDB).filter(PostDB.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    db.delete(post)
    db.commit()
    return {"mensaje": "Post eliminado"}
