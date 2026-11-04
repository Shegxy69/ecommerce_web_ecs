from fastapi import FastAPI
from pydantic import BaseModel
import os
import time

app = FastAPI(title="Payment Service", version="1.0.0")
START_TIME = time.time()

class Item(BaseModel):
    name: str
    value: float = 0

@app.get("/health")
def health():
    return {
        "service": "payment-service",
        "status": "healthy",
        "environment": os.getenv("APP_ENV", "local"),
        "uptime_seconds": round(time.time() - START_TIME, 2),
    }

@app.get("/ready")
def ready():
    return {"ready": True, "service": "payment-service"}

@app.get("/payments")
def list_items():
    return {
        "service": "payment-service",
        "items": [
            {"id": 1, "name": "demo-item", "status": "active"}
        ]
    }

@app.post("/payments")
def create_item(item: Item):
    return {
        "service": "payment-service",
        "created": True,
        "item": item.model_dump()
    }
