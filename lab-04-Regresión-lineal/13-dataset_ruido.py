# Ejercicio 13
# Simula un dataset con una variable aleatoria (ruido) sin relación con la salida. Entrena un modelo y explica
# por qué falla.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.datasets import make_regression
import tkinter as tk
from tkinter import messagebox

# Simular un dataset con ruido con make_regression
X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)

X_noise = np.random.rand(100, 1) * 100  # Ruido aleatorio
# Convertir a DataFrame
df = pd.DataFrame(X, columns=['Feature'])
df['variable_Noise'] = X_noise.flatten()
df['Target'] = y
# Mostrar las primeras filas del DataFrame
print(df.head(3))
# Dividir el dataset en conjunto de entrenamiento y conjunto de prueba
#X = df[['Feature', 'variable_Noise']]
X = df[['variable_Noise']]  # Solo la variable de ruido
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Crear el modelo de regresión lineal
model = LinearRegression()
# Entrenar el modelo
model.fit(X_train, y_train)
# Hacer predicciones
y_pred = model.predict(X_test)
# Mostrar las primeras predicciones
print("Predicciones de la variable objetivo:")
print(y_pred[:5])
# Calcular el error absoluto medio (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f"Error Absoluto Medio (MAE): {mae:.2f}")
# Calcular el error cuadrático medio (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
# Mostrar el coeficiente de determinación R^2
r2 = r2_score(X_test, y_test)
print(f"Coeficiente de determinación R^2: {r2:.2f}")


root = tk.Tk()
root.withdraw()  # Oculta la ventana principal
messagebox.showinfo(f"Valor Coeficiente R2 {r2}  :", "indica que el modelo de regresión lineal no solo no explica la variabilidad de la variable objetivo, sino que lo hace peor que una simple media. Esto ocurre porque la variable usada (en este caso, ruido aleatorio) no tiene relación con la variable objetivo.")