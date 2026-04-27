from fastapi import FastAPI
from pydantic import BaseModel, Field
import numpy as np
import joblib

app = FastAPI()

# Load model
model = joblib.load("model.pkl")


# 🔥 Define request schema
class InputData(BaseModel):
    temperature: float = Field(..., ge=-10, le=60)
    hour: int = Field(..., ge=0, le=23)

@app.get("/")
def home():
    return {"message": "Professional Energy API 🚀"}


@app.post("/predict")
def predict(data: InputData):

    # Extract values
    temperature = data.temperature
    hour = data.hour

    # Features
    hour_sin = np.sin(2 * np.pi * hour / 24)
    hour_cos = np.cos(2 * np.pi * hour / 24)

    features = [[temperature, hour_sin, hour_cos]]

    pred = model.predict(features)

    return {
        "input": data,
        "predicted_kWh": float(pred[0])
    }