# **Conclusiones del Proyecto: Análisis Comparativo**

## **Rendimiento Computacional: ¿Qué modelo fue más eficiente?**

**LightGBM y XGBoost** demostraron superioridad en velocidad de inferencia:

Ambos modelos registraron los menores tiempos de predicción (~0.020 s), gracias a sus implementaciones altamente optimizadas de gradient boosting y procesamiento paralelo.

**CatBoost** obtuvo un tiempo intermedio (0.028 s), influido por su manejo interno de variables categóricas.

**Random Forest** fue el más lento (0.071 s), debido a la evaluación independiente de numerosos árboles sin optimizaciones de boosting.

**Veredicto:**
Todos los modelos presentan tiempos de predicción muy bajos (<0.08 s), adecuados para entornos en tiempo real. Sin embargo, LightGBM y XGBoost ofrecen la mejor relación entre velocidad y rendimiento predictivo.

## **Precisión Predictiva: ¿Cuál logró el mejor equilibrio?**

CatBoost alcanzó el mejor rendimiento global:

| Modelo | AUC-ROC | Precision | Recall | F1-Score | Accuracy |
|--------|----------|-----------|--------|----------| ----------|
| **Catboost** | 0.8365 | 0.504188 | 0.804813 | 0.619979 | 0.737740 |
| **XGBoost** | 0.8341 | 0.653430 | 0.483957 | 0.556068 | 0.794598 |
| **RandomForest** | 0.8331 | 0.515888 | 0.737968 | 0.607261 | 0.746269 |
| **LightGBM** | 0.8327 | 0.661818 | 0.486631 | 0.560863 | 0.797441 |

## **Aplicabilidad: ¿Cuándo usar cada modelo?**

Usar **CatBoost** cuando:

- Se prioriza detectar la mayor cantidad de casos positivos (recall alto).

- Se trabaja con variables categóricas complejas.

- Se dispone de recursos computacionales moderados (tiempo de inferencia medio).

Usar **LightGBM o XGBoost** cuando:

- Se requiere alta precisión y baja latencia (tiempo de respuesta mínimo).

- Se busca robustez y estabilidad en producción.

- Se necesita un modelo fácil de escalar y actualizar rápidamente.

Usar **Random Forest** cuando:

- Se desea un modelo simple y estable, ideal para baselines o sistemas con interpretabilidad prioritaria.

## **Interpretabilidad: ¿Qué aportó LIME?**

LIME fue clave para comprender las decisiones individuales de cada modelo y comprender qué variables impulsaron o frenaron las predicciones de churn:

- Factores protectores (reducen la probabilidad de churn):
`Contract_Two year`, `Contract_One year`, `TotalCharges` altos, `tenure` largo y `PaymentMethod ≠ Electronic check`.

- Factores de riesgo (aumentan la probabilidad de churn):
`InternetService = Fiber optic`, `MonthlyCharges` altos y `StreamingMovies = Yes`.

LIME evidenció que, aunque todos los modelos reconocen los mismos patrones generales, su forma de ponderar las variables difiere. Esto permitió validar la coherencia de las decisiones y detectar sesgos específicos, como la sobrepenalización del servicio de fibra óptica. Además, aportó transparencia y explicabilidad, permitiendo entender las decisiones del modelo, validar la lógica de negocio y detectar posibles sesgos.
