from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_predict_endpoint():
    payload = {
    "model_name": "Random Forest", 
    "data": {
        "SeniorCitizen": 0,
        "MonthlyCharges": 70.35,
        "TotalCharges": 1397.475,
        "tenure": 24,
        "gender": 0,
        "Partner": 1,
        "Dependents": 0,
        "PhoneService": 1,
        "PaperlessBilling": 1, 
        "MultipleLines": "Yes",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaymentMethod": "Electronic check"
    }
} 

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "churn_probability" in data
    assert "prediction" in data