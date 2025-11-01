# app/models.py
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from .database import Base

# 用户表（后续会扩展）
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    # 与日记表建立一对多关系
    diaries = relationship("Diary", back_populates="author")

# 日记表
class Diary(Base):
    __tablename__ = "diaries"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    is_shared = Column(Boolean, default=False)  # 是否公开分享
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    author_id = Column(Integer, ForeignKey("users.id"))

    # 建立反向引用（方便查询作者信息）
    author = relationship("User", back_populates="diaries")
