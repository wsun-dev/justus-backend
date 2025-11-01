# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

# 创建日记
def create_diary(db: Session, diary: schemas.DiaryCreate, user_id: int):
    db_diary = models.Diary(**diary.dict(), author_id=user_id)
    db.add(db_diary)
    db.commit()
    db.refresh(db_diary)
    return db_diary

# 获取所有共享日记
def get_shared_diaries(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Diary).filter(models.Diary.is_shared == True).offset(skip).limit(limit).all()

# 根据用户ID获取自己的日记
def get_user_diaries(db: Session, user_id: int):
    return db.query(models.Diary).filter(models.Diary.author_id == user_id).all()

# 删除日记
def delete_diary(db: Session, diary_id: int, user_id: int):
    diary = db.query(models.Diary).filter(models.Diary.id == diary_id, models.Diary.author_id == user_id).first()
    if diary:
        db.delete(diary)
        db.commit()
    return diary
