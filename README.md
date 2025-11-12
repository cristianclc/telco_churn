<h2 align="center">Vídeo demostración del Proyecto</h2>

<p align="center">
  <img src="assets/demostracion.gif" width="600" alt="Vista previa de la API">
</p>

# Predicción de Churn en Telecomunicaciones

## Descripción
Este proyecto implementa diversos modelos de Machine Learning para predecir el abandono de clientes (churn) en una empresa de telecomunicaciones.
Incluye modelos como Random Forest, XGBoost, CatBoost y LightGBM, empaquetados dentro de una API REST desarrollada con FastAPI y desplegable mediante Docker.

## Componentes
- `notebooks/`: Análisis exploratorio, entrenamiento y explicabilidad.
- `app/api.py`: API REST para predicciones.
- `Dockerfile`: Configuración para despliegue.

## Instalación
```bash
git clone https://github.com/cristianclc/telco_churn.git
cd telco_churn
pip install -r requirements.txt
```
Abrimos Docker Desktop

Construimos la imagen Docker

## Docker
```bash
docker build -t telco-churn .
docker run -d --name telco-churn-container -p 8000:8000 telco-churn
```
Verificamos que la imagen está ejecutando con:

```bash
docker ps
```

## Probamos la API

Una vez el contenedor esté corriendo, la API estará disponible en: http://127.0.0.1:8000/docs
Dentro del enlace, enviamos un `POST` a `/predict` con un JSON como este:

```json
{
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
```

Lo que nos retornará:

```json
{
  "model_used": "string", 
  "churn_probability": 0,
  "prediction": 0
}
```
- `model_used`: corresponde al modelo seleccionado, las opciones pueden ser: `Random Forest`, `XGBoost`, `Catboost`, `LightGBM`.

- `churn_probability`: Probabilidad de que el cliente decida darse de baja.

- `prediction`: Predicción final del modelo.

## Autores
- Cristian Linero
- David Marquez