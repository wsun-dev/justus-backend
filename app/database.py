# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# 从环境变量获取数据库连接（来自 docker-compose.yml）
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://justus:justus123@db:5432/justus_db")

# 创建数据库引擎
engine = create_engine(DATABASE_URL)

# 创建Session类，用于与数据库交互
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 基类，用于定义模型
Base = declarative_base()

# FastAPI依赖项：每次请求都会获得独立数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
