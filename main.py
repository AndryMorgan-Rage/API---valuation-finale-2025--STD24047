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
phone_db_mise_A_jour: List[Phone] = []
@app.post("/phone", status_code=status.HTTP_201_CREATED)
def create_phone(phone: Phone):
    phones.append(phone)
    return {"message": "Phone create success", "phone": phone}
@app.post("/phone", status_code=201)
def create_phone(phone: Phone):
    phones_db.append(phone)
    return {"message": "Phone add success"}

@app.get("/phones", response_model=List[Phone])
def get_phones():
    return phones
@app.get("/phones/{identifier}", response_model=Phone)
def get_phone(identifier: str):
    for phone in phones_db:
        if phone.identifier == identifier:
            return phone
    raise HTTPException(status_code=404, detail=f"Phone avec id '{identifier}' not found")

@app.put("/phones/{identifier}/characteristic", response_model=Phone)
def update_characteristic(identifier: str, new_characteristic: Caracteristique):
    for phone in phone_db_mise_A_jour:
        if phone.identifier == identifier:
            phone.characteristique = new_characteristic
            return phone
    raise HTTPException(status_code=404, detail=f"Phone avec id '{identifier}' not found")


