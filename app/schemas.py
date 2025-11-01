# app/schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# 创建和更新时使用的基础模型
class DiaryBase(BaseModel):
    title: str
    content: str
    is_shared: Optional[bool] = False

# 创建时使用
class DiaryCreate(DiaryBase):
    pass

# 返回给前端的模型
class Diary(DiaryBase):
    id: int
    created_at: datetime
    author_id: int

    class Config:
        orm_mode = True
