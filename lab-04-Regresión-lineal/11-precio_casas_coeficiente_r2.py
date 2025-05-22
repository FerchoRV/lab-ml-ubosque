# Ejercicio 11
# Calcula el coeficiente de determinación R2 del modelo en el ejercicio 10. Interprétalo.

import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import messagebox

# Cargar el dataset California Housing
california = fetch_california_housing()

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
# Mostrar el coeficiente de determinación R^2
r2_score = model.score(X_test, y_test)
print(f"Coeficiente de determinación R^2: {r2_score:.2f}")
# Mostrar los coeficientes del modelo

root = tk.Tk()
root.withdraw()  # Oculta la ventana principal
messagebox.showinfo(f"Valor Coeficiente R2 {r2_score} :", "Un coeficiente de determinación R² = 0.58 significa que el modelo de regresión lineal explica aproximadamente el 58% de la variabilidad en los precios de las casas a partir de las variables independientes del dataset. \n Hay un 42% de la variabilidad en los precios que no es explicada por el modelo, posiblemente debido a factores no incluidos o a la naturaleza lineal del modelo. El modelo puede ser útil para hacer predicciones generales, pero no es completamente preciso. Podrías mejorar el desempeño usando modelos más complejos o agregando más variables relevantes.")