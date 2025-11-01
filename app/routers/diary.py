# app/routers/diary.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, crud, models
from ..database import get_db

router = APIRouter(
    prefix="/diaries",
    tags=["diaries"]
)

# 临时：假设用户ID固定为1（之后我们加JWT登录）
USER_ID = 1

@router.post("/", response_model=schemas.Diary)
def create_diary(diary: schemas.DiaryCreate, db: Session = Depends(get_db)):
    """创建新日记"""
    return crud.create_diary(db=db, diary=diary, user_id=USER_ID)

@router.get("/shared", response_model=List[schemas.Diary])
def read_shared_diaries(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """查看所有共享日记"""
    return crud.get_shared_diaries(db, skip=skip, limit=limit)

@router.get("/me", response_model=List[schemas.Diary])
def read_my_diaries(db: Session = Depends(get_db)):
    """查看自己的日记"""
    return crud.get_user_diaries(db, user_id=USER_ID)

@router.delete("/{diary_id}")
def delete_my_diary(diary_id: int, db: Session = Depends(get_db)):
    """删除自己的日记"""
    diary = crud.delete_diary(db, diary_id=diary_id, user_id=USER_ID)
    if diary is None:
        raise HTTPException(status_code=404, detail="未找到该日记或无权限删除")
    return {"message": "日记已删除"}
