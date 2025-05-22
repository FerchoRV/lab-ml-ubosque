# Ejercicio 14
# Divide un dataset en 80% entrenamiento y 20% prueba. Evalúa el rendimiento en ambos subconjuntos.

import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


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

#evaluar el rendimiento en el conjunto de entrenamiento
y_train_pred = model.predict(X_train)
#calcular R2
r2_train = r2_score(y_train, y_train_pred)
#calcular MAE
mae_train = mean_absolute_error(y_train, y_train_pred)
#calcular MSE
mse_train = mean_squared_error(y_train, y_train_pred)
print(f"R2 en el conjunto de entrenamiento: {r2_train:.2f}")
print(f"Error Absoluto Medio (MAE) en el conjunto de entrenamiento: {mae_train:.2f}")
print(f"Error Cuadrático Medio (MSE) en el conjunto de entrenamiento: {mse_train:.2f}")
# Evaluar el rendimiento en el conjunto de prueba
y_test_pred = model.predict(X_test)
# Calcular R2
r2_test = r2_score(y_test, y_test_pred)
# Calcular MAE
mae_test = mean_absolute_error(y_test, y_test_pred)
# Calcular MSE
mse_test = mean_squared_error(y_test, y_test_pred)
print(f"R2 en el conjunto de prueba: {r2_test:.2f}")
print(f"Error Absoluto Medio (MAE) en el conjunto de prueba: {mae_test:.2f}")
print(f"Error Cuadrático Medio (MSE) en el conjunto de prueba: {mse_test:.2f}")

