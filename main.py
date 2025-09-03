from fastapi import FastAPI
from starlette.responses import JSONResponse
from pydantic import BaseModel

from starlette.requests import Request

app = FastAPI()

@app.get("/health")
def health():
    return {"message":"Ok"}

