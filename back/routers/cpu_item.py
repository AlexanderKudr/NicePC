from fastapi import APIRouter, Depends, File, UploadFile, Form
from routers.schemas import CpuItemBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_cpu_item
import shutil
import json
from fastapi.exceptions import HTTPException


router = APIRouter(
    prefix='/cpu_item',
    tags=['cpu_item']
)

@router.post('/123')
def create_cpu_item(request: str = Form(), image: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        item = CpuItemBase.parse_obj(json.loads(request))
    except :
        raise HTTPException(status_code=422, detail='kostyl pizdes')
    path = f'images/{image.filename}'
    with open(path, 'wb+') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return db_cpu_item.create_cpu(db, item, path)


@router.get('/')
def get_all_cpus(db: Session = Depends(get_db)):
    return db_cpu_item.get_all_cpu(db)


@router.post('/delete')
def delete_cpu_item(id: int, db: Session = Depends(get_db)):
    return db_cpu_item.delete(db, id)