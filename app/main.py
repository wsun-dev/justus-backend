from fastapi import FastAPI

app = FastAPI(title="Justus Shared Diary")

@app.get("/")
def root():
    return {"message": "Justus backend is running 🚀"}
