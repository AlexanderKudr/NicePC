from routers.schemas import Cart
from sqlalchemy.orm import Session, joinedload
from db.models import DbUserCart, DbItem
from fastapi import HTTPException, status
from dotenv import load_dotenv
import os
import psycopg2


load_dotenv()

def add_item_to_cart(db: Session, request: Cart, user_id):
    new_item = DbUserCart(
        user_id = user_id,
        product_id = request.product_id
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def get_items(user_id: int):
    connection = psycopg2.connect(
                host=os.getenv('DB_HOST'),
                database=os.getenv('DB_DATABASE'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD')
            )


    query = "SELECT items.*, cart_items.id AS cart_item_id FROM cart_items JOIN items ON cart_items.product_id = items.id WHERE user_id = {}".format(user_id)

    cursor = connection.cursor()
    cursor.execute(query)
    col_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()

    response = []
    for row in rows:
        item = {}
        for i in range(len(col_names)):
            item[col_names[i]] = row[i]
        response.append(item)
    return response


def delete(item_id, db: Session, user_id: int):
    item = db.query(DbUserCart).filter(DbUserCart.id == item_id).first()
    if item.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.delete(item)
    db.commit()
    return 'okay'


def delete_all_cart_items(db: Session, user_id: int):
    items = db.query(DbUserCart).filter(DbUserCart.user_id == user_id).all()
    for item in items:
        db.delete(item)
    db.commit()
    return 'okay'