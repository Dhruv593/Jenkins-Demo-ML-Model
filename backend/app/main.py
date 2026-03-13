from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# 🔓 OPEN CORS FOR LOCAL TESTING
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

ML_SERVICE_URL = "http://ml-service:8001/predict"

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictionResponse(BaseModel):
    class_name: str

@app.post("/predict", response_model=PredictionResponse)
def predict(data: IrisInput):
    response = requests.post(ML_SERVICE_URL, json=data.dict(), timeout=5)
    return {"class_name": response.json()["class"]}