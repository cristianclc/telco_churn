from pydantic import BaseModel


class CustomerData(BaseModel):
    SeniorCitizen: int
    MonthlyCharges: float
    TotalCharges: float
    tenure: int
    gender: int
    Partner: int
    Dependents: int
    PhoneService: int
    PaperlessBilling: int
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaymentMethod: str


class PredictionRequest(BaseModel):
    model_name: str
    data: CustomerData


class PredictionResponse(BaseModel):
    model_used: str
    churn_probability: float
    prediction: int
