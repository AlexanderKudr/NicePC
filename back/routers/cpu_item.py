from fastapi import APIRouter, Depends
from routers.schemas import CpuItemBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_cpu_item


router = APIRouter(
    prefix='/cpu_item',
    tags=['cpu_item']
)

@router.post('/')
def create_cpu_item(request: CpuItemBase, db: Session = Depends(get_db)):
    return db_cpu_item.create_cpu(db, request)


@router.get('/')
def get_all_cpus(db: Session = Depends(get_db)):
    return db_cpu_item.get_all_cpu(db)

@router.post('/delete')
def delete_cpu_item(id: int, db: Session = Depends(get_db)):
    return db_cpu_item.delete(db, id)