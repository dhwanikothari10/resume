from fastapi import FastAPI
from src.router import router, get, delete
from database.conn import db

app = FastAPI(title="Resume PDF Summarizer")

app.include_router(router.router)
app.include_router(get.router)
app.include_router(delete.router)


@app.get("/")
def root():
    return {"message": "Resume Summarizer API is running"}
