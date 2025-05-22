# Ejercicio 10
# Carga un dataset real desde sklearn.datasets como Boston Housing o uno de Kaggle, aplica regresión lineal
# para predecir precios.

import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Cargar el dataset California Housing
california = fetch_california_housing()
# Convertir a DataFrame
california_df = pd.DataFrame(data=california.data, columns=california.feature_names)
# Añadir la variable objetivo
california_df['PRICE'] = california.target
# Mostrar las primeras filas del DataFrame
print(california_df.head(3))
# Dividir el dataset en características y variable objetivo
X = california_df.drop('PRICE', axis=1)
y = california_df['PRICE']
# Dividir el dataset en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Crear el modelo de regresión lineal
model = LinearRegression()
# Entrenar el modelo
model.fit(X_train, y_train)
# Hacer predicciones
y_pred = model.predict(X_test)
# Mostrar las primeras predicciones
print("Predicciones de precios de casas:")
print(y_pred[:5])

