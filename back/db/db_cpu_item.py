from routers.schemas import FrontPostBase
from sqlalchemy.orm import Session
from db.models import DbFrontPost
from fastapi import HTTPException, status


def create_post(db: Session, request: FrontPostBase):
    new_post = DbFrontPost(
        title = request.title,
        body = request.body
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post



def get_all_posts(db: Session):
    return db.query(DbFrontPost).all()


def delete(db: Session, id: int):
    post = db.query(DbFrontPost).filter(DbFrontPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Post with id {id} not found')
    db.delete(post)
    db.commit()
    return 'okay'