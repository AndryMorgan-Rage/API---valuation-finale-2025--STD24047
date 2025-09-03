from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/health")
def health():
    return {"message":"Ok"}
class Characteristic(BaseModel):
    ram_memory: int
    rom_memory: int
class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristic: Characteristic
phones: List[Phone] = []
@app.post("/phone", status_code=status.HTTP_201_CREATED)
def create_phone(phone: Phone):
    phones.append(phone)
    return {"message": "Phone created successfully", "phone": phone}
@app.post("/phone", status_code=201)
def create_phone(phone: Phone):
    phones_db.append(phone)
    return {"message": "Phone added successfully"}

@app.get("/phones", response_model=List[Phone])
def get_phones():
    return phones
