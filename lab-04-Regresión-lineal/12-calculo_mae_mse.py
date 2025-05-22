# Ejercicio 12
# Ajusta una regresión lineal y muestra el error absoluto medio (MAE) y el error cuadrático medio (MSE).

import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Cargar el dataset de diabetes
diabetes = load_diabetes()
# Convertir a DataFrame
diabetes_df = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)
# Añadir la variable objetivo
diabetes_df['DIABETES'] = diabetes.target
# Mostrar las primeras filas del DataFrame
print(diabetes_df.head(3))
# Dividir el dataset en características y variable objetivo
X = diabetes_df.drop('DIABETES', axis=1)
y = diabetes_df['DIABETES']
# Dividir el dataset en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Crear el modelo de regresión lineal
model = LinearRegression()
# Entrenar el modelo
model.fit(X_train, y_train)
# Hacer predicciones
y_pred = model.predict(X_test)
# Mostrar las primeras predicciones
print("Predicciones de diabetes:")
print(y_pred[:5])
# Calcular el error absoluto medio (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f"Error Absoluto Medio (MAE): {mae:.2f}")
# Calcular el error cuadrático medio (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
