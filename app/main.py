from fastapi import FastAPI
from .routers import diary
from . import models
from .database import engine

# 自动创建表
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Justus 电子共享日记")

# 注册日记路由
app.include_router(diary.router)

@app.get("/")
def root():
    return {"message": "Justus backend is running"}
