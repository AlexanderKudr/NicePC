from fastapi import APIRouter, Depends, File, UploadFile, Form
from routers.schemas import ItemBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_item
import shutil
import json
from fastapi.exceptions import HTTPException


router = APIRouter(
    prefix='/item',
    tags=['item']
)

@router.post('/')
def create_item(request: str = Form(), image: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        item = ItemBase.parse_obj(json.loads(request))
    except :
        raise HTTPException(status_code=422, detail='kostyl pizdes')
    path = f'images/item_image/{image.filename}'
    with open(path, 'wb+') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return db_item.db_create_item(db, item, path)


@router.post('/delete')
def delete_item(id: int, db: Session = Depends(get_db)):
    return db_item.db_delete_item(db, id)


@router.get('/')
def get_all_items(type_id: str, db: Session = Depends(get_db)):
    return db_item.db_get_all_items(db, type_id)

@router.get('/one')
def get_one_item(item_id: str, db: Session = Depends(get_db)):
    return db_item.db_get_one_item(db, item_id)


