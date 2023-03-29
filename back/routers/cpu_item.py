from fastapi import APIRouter, Depends
from routers.schemas import FrontPostBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_frontend_posts


router = APIRouter(
    prefix='/cpu_item',
    tags=['cpu_item']
)

@router.post('/')
def create_cpu_item(request: FrontPostBase, db: Session = Depends(get_db)):
    return db_frontend_posts.create_post(db, request)


@router.get('/')
def get_all_posts(db: Session = Depends(get_db)):
    return db_frontend_posts.get_all_posts(db)

@router.post('/delete')
def delete_post(id: int, db: Session = Depends(get_db)):
    return db_frontend_posts.delete(db, id)