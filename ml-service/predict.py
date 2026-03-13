from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import numpy as np

app = FastAPI()

# Load trained model
model = load("model/iris_model.pkl")

CLASS_NAMES = ["Setosa", "Versicolor", "Virginica"]

# ---- Request schema ----
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/health")
def health():
    return {"status": "ok"}
# ---- Prediction endpoint ----
@app.post("/predict")
def predict(data: IrisInput):
    features = np.array([
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]).reshape(1, -1)

    prediction = model.predict(features)[0]

    return {
        "class": CLASS_NAMES[prediction]
    }