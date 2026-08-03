# Customer Churn Prediction API & Power BI Dashboard
A Machine Learning API built with FastAPI and XGBoost to predict customer churn based on customer demographics, subscription details, and service usage.
Interactive Power BI dashboard for business intelligence, customer segmentation, revenue analysis, and machine learning insights.
## Dashboard Preview

### Executive Overview

![Executive Overview](images/ccustomer_churn_overview.png)

## Features

- Customer churn prediction
- Probability score for each prediction
- REST API with FastAPI
- Interactive Swagger documentation
- Interactive Power BI Dashboard
- Business KPI Monitoring
- Customer Churn Analysis
- Revenue Analysis
- Machine Learning Model Insights

## Technologies

- Python
- FastAPI
- XGBoost
- Scikit-learn
- Pandas
- Joblib
- Power BI
- Azure App Service

## Project Structure

```text
Customer-Churn-Prediction-API/
│
├── app.py
├── requirements.txt
├── README.md
│
├── Dashboard/
│   └── customerchurnpowerbi.pdf
│
├── images/
│   ├── customer_churn_overview.png
│   ├── customer_churn_customer_analysis.png
│   ├── customer_churn_revenue_analysis.png
│   ├── customer_churn_model_insights.png
    ├── logistic_matrix.png
    ├── randomforest_matrix.png
    ├── xgboost_matrix.png
    ├── azure-live-demo.png
    ├── local-live-demo.png
│   └── feature_importance.png
│
└── model/
    ├── xgboost_churn_model.pkl
    ├── scaler.pkl
    └── label_encoders.pkl
```

## Installation

```bash
pip install -r requirements.txt
python -m uvicorn app:app --reload
```
## Live Demo

### Azure REST API (Swagger)

https://customer-churn-api-ezgi-e8bsbagubrbvf6a3.swedencentral-01.azurewebsites.net/docs

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

## Example Request

```json
{
  "Gender": "Female",
  "Senior_Citizen": "No",
  "Partner": "Yes",
  "Dependents": "No",
  "Tenure_Months": 24,
  "Phone_Service": "Yes",
  "Multiple_Lines": "No",
  "Internet_Service": "Fiber optic",
  "Online_Security": "No",
  "Online_Backup": "Yes",
  "Device_Protection": "No",
  "Tech_Support": "No",
  "Streaming_TV": "Yes",
  "Streaming_Movies": "Yes",
  "Contract": "Month-to-month",
  "Paperless_Billing": "Yes",
  "Payment_Method": "Electronic check",
  "Monthly_Charges": 89.5,
  "Total_Charges": 2100
}
```

## Example Response

```json
{
  "prediction": "Yes",
  "probability": 0.7407
}
```

## Model Performance

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|------|---------:|----------:|-------:|----:|--------:|
| Logistic Regression | 0.741 | 0.508 | 0.783 | 0.616 | 0.841 |
| Random Forest | 0.760 | 0.541 | 0.655 | 0.593 | 0.817 |
| XGBoost | **0.775** | **0.566** | **0.652** | **0.606** | **0.839** |

**XGBoost** was selected as the final model due to its strong overall performance and balanced classification metrics.

## Power BI Dashboard

The project also includes an interactive Power BI dashboard for business intelligence and customer churn analysis.

Dashboard Pages

- Executive Overview
- Customer Analysis
- Revenue Analysis
- Model Insights

### Executive Overview

![Executive Overview](images/ccustomer_churn_overview.png)

---

### Customer Analysis

![Customer Analysis](images/customer_churn_customer_analysis.png)

---

### Revenue Analysis

![Revenue Analysis](images/customer_churn_revenue_analysis.png)

---

### Model Insights

![Model Insights](images/customer_churn_model_insights.png)

## Project Highlights

- End-to-End Machine Learning Project
- Customer Churn Prediction with XGBoost
- REST API built using FastAPI
- Cloud Deployment on Azure App Service
- Interactive Power BI Dashboard

## Dashboard

📄 Power BI Dashboard PDF

[Download Dashboard](Dashboard/customerchurnpowerbi.pdf)

## Author

**Zeynep Ezgi Yakışan**

Management Information Systems Student

Machine Learning • Data Science • Power BI • Azure
