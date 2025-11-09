import os
import joblib
import pytest
import pandas as pd
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))
RUTA_MODELOS = os.path.abspath(os.path.join(current_dir,"..", "app", "models.joblib"))

@pytest.fixture(scope="module")
def modelos():
    models = joblib.load(RUTA_MODELOS)
    assert isinstance(models, dict), "El archivo de modelos no contiene un diccionario."
    return models


@pytest.fixture
def sample_input():
    return pd.DataFrame([{
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
    }])


def test_modelos_cargan_correctamente(modelos):
    esperados = {"Random Forest", "XGBoost", "Catboost", "LightGBM"}
    assert set(modelos.keys()) == esperados, f"Modelos esperados: {esperados}, encontrados: {modelos.keys()}"


def test_predicciones_funcionan(modelos, sample_input):
    for nombre, pipeline in modelos.items():
        try:
            proba = pipeline.predict_proba(sample_input)[0][1]
            assert 0 <= proba <= 1, f"La probabilidad del modelo {nombre} no está entre 0 y 1."
        except Exception as e:
            pytest.fail(f"El modelo {nombre} falló al predecir: {e}")