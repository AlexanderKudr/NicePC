from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from routers.schemas import CommentBase, UserAuth
from auth.oauth2 import get_current_user
from db.database import get_db
from db.db_comment import create_comment, get_all

router = APIRouter(
    prefix='/comment',
    tags=['comment']
)

@router.post('/')
def new_comment(request: CommentBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return create_comment(db, request)


@router.get('/all/{post_id}')
def get_all_comments(post_id: int, db: Session = Depends(get_db)):
    return get_all(db, post_id)