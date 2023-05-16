from fastapi import APIRouter, Depends, status
from routers.schemas import Cart
from sqlalchemy.orm import Session
from db.database import get_db
from fastapi import HTTPException
from db import db_cart
from typing import List
from routers.schemas import UserAuth
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/cart',
    tags=['cart']
)


@router.post('/')
def add_item(request: Cart, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_cart.add_item_to_cart(db, request, current_user.id)


@router.get('/')
def get_user_items(current_user: UserAuth = Depends(get_current_user)):
    return db_cart.get_items(current_user.id)


@router.get('/delete/{id}')
def delete_item(id: int, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_cart.delete(id, db, current_user.id)

@router.get('/del/all')
def delete_all_user_items(db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_cart.delete_all_cart_items(db, current_user.id)


