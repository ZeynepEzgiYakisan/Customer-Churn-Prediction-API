from fastapi import FastAPI
from pydantic import BaseModel

import pandas as pd
import joblib

import os
import joblib
# --------------------------------------------------
# Create FastAPI App
# --------------------------------------------------

app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0.0"
)

# --------------------------------------------------
# Load Model
# --------------------------------------------------


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(
    os.path.join(BASE_DIR, "model", "xgboost_churn_model.pkl")
)

scaler = joblib.load(
    os.path.join(BASE_DIR, "model", "scaler.pkl")
)

label_encoders = joblib.load(
    os.path.join(BASE_DIR, "model", "label_encoders.pkl")
)

# --------------------------------------------------
# Request Body
# --------------------------------------------------

class Customer(BaseModel):

    Gender: str
    Senior_Citizen: str
    Partner: str
    Dependents: str

    Tenure_Months: int

    Phone_Service: str
    Multiple_Lines: str

    Internet_Service: str
    Online_Security: str
    Online_Backup: str
    Device_Protection: str
    Tech_Support: str

    Streaming_TV: str
    Streaming_Movies: str

    Contract: str
    Paperless_Billing: str
    Payment_Method: str

    Monthly_Charges: float
    Total_Charges: float


# --------------------------------------------------
# Home
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "Customer Churn Prediction API is running!"
    }


# --------------------------------------------------
# Predict
# --------------------------------------------------

@app.post("/predict")
def predict(customer: Customer):

    data = {
        "Gender": customer.Gender,
        "Senior Citizen": customer.Senior_Citizen,
        "Partner": customer.Partner,
        "Dependents": customer.Dependents,
        "Tenure Months": customer.Tenure_Months,
        "Phone Service": customer.Phone_Service,
        "Multiple Lines": customer.Multiple_Lines,
        "Internet Service": customer.Internet_Service,
        "Online Security": customer.Online_Security,
        "Online Backup": customer.Online_Backup,
        "Device Protection": customer.Device_Protection,
        "Tech Support": customer.Tech_Support,
        "Streaming TV": customer.Streaming_TV,
        "Streaming Movies": customer.Streaming_Movies,
        "Contract": customer.Contract,
        "Paperless Billing": customer.Paperless_Billing,
        "Payment Method": customer.Payment_Method,
        "Monthly Charges": customer.Monthly_Charges,
        "Total Charges": customer.Total_Charges
    }

    df = pd.DataFrame([data])

    # Encode categorical columns
    categorical_columns = [
        "Gender",
        "Senior Citizen",
        "Partner",
        "Dependents",
        "Phone Service",
        "Multiple Lines",
        "Internet Service",
        "Online Security",
        "Online Backup",
        "Device Protection",
        "Tech Support",
        "Streaming TV",
        "Streaming Movies",
        "Contract",
        "Paperless Billing",
        "Payment Method"
    ]

    for column in categorical_columns:
        df[column] = label_encoders[column].transform(df[column])

    # Scale only numerical columns
    numerical_columns = [
        "Tenure Months",
        "Monthly Charges",
        "Total Charges"
    ]

    df[numerical_columns] = scaler.transform(df[numerical_columns])

    # Prediction
    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    result = "Yes" if prediction == 1 else "No"

    return {
        "prediction": result,
        "probability": round(float(probability), 4)
    }