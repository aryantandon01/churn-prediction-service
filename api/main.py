# api/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from churn_service.predictor import load_model
from churn_service.config import MODEL_PATH
import pandas as pd
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

# Load model at startup
clf = load_model(MODEL_PATH)

# Define expected JSON input (example: all needed features)
class CustomerFeatures(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: int
    PhoneService: int
    MultipleLines: int
    InternetService: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    Contract: int
    PaperlessBilling: int
    PaymentMethod: int
    MonthlyCharges: float
    TotalCharges: float

@app.get("/")
def read_root():
    return {"message": "Churn prediction API is up!"}

@app.post("/predict")
def predict_churn(features: CustomerFeatures):
    logging.info("Received prediction request")
    # Convert incoming JSON to dataframe
    data = pd.DataFrame([features.dict()])

    # Predict churn (0 or 1)
    pred = clf.predict(data)[0]
    prob = clf.predict_proba(data)[0][1]

    return {
        "churn_prediction": int(pred),
        "churn_probability": round(float(prob), 4)
    }
