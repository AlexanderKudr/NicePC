from routers.schemas import ItemBase
from sqlalchemy.orm import Session
from db.models import DbItem
from fastapi import HTTPException, status


def db_create_item(db: Session, request: ItemBase, path):
    new_item = DbItem(
        type_id = request.type_id,
        name = request.name,
        param1 = request.param1,
        param2 = request.param2,
        param3 = request.param3,
        param4 = request.param4,
        param5 = request.param5,
        param6 = request.param6,
        param7 = request.param7,
        price = request.price,
        image = path
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def db_delete_item(db: Session, id: int):
    cpu = db.query(DbItem).filter(DbItem.id == id).first()
    if not cpu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Cpu with id {id} not found')
    db.delete(cpu)
    db.commit()
    return 'okay'


def db_get_all_items(db: Session, type_id: str):
    return db.query(DbItem).filter(DbItem.type_id == type_id).all()


def db_get_one_item(db: Session, item_id):
    return db.query(DbItem).filter(DbItem.id == item_id).first()