# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}