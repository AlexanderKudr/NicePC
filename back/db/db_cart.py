from routers.schemas import Cart
from sqlalchemy.orm import Session
from db.models import DbUserCart, DbCpuItem
from fastapi import HTTPException, status


def add_item_to_cart(db: Session, request: Cart, user_id):
    new_item = DbUserCart(
        user_id = user_id,
        product_id = request.product_id
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def get_items(db: Session, user_id: int):
    item_ids = db.query(DbUserCart).filter(DbUserCart.user_id == user_id).all()
    # user_items = db.query(DbCpuItem).filter(DbCpuItem.id == item_ids.product_id).all()
    return item_ids


def delete(item_id, db: Session, user_id: int):
    item = db.query(DbUserCart).filter(DbUserCart.id == item_id).first()
    if item.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(item)
    db.commit()
    return 'okay'