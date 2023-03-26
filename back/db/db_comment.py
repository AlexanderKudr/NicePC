from routers.schemas import CommentBase
from sqlalchemy.orm import Session
from db.models import DbComment
from datetime import datetime
from fastapi import HTTPException
from fastapi import status
from db.models import DbComment

def create_comment(db: Session, request: CommentBase):
    new_comment = DbComment(
        text = request.text,
        username = request.username,
        timestamp = datetime.now(),
        post_id = request.post_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment



def get_all(db: Session):
    return db.query(DbComment).all()