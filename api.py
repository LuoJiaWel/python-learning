from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Record(BaseModel):
    date: str
    category: str
    expense: float
    remark: str

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

@app.get("/about")
def about():
    return {
        "project": "Money Tracker",
        "language": "python",
        "database": "SQLite"
    }

@app.get("/records/{record_id}")
def get_record(record_id: int):
    return {
        "record_id":record_id
    }

@app.get("/search")
def search_records(category: str):
    return {
        "category": category,
        "message": f"查詢類別：{category}"
    }

@app.post("/records")
def create_record(record: Record):
    return {
        "message": "收到記帳資料",
        "record": record
    }