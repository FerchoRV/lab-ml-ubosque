# Ejercicio 7
# Simula datos sobre edad y frecuencia cardíaca. Aplica regresión lineal y analiza si la relación es positiva o
# negativa.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import messagebox

# Datos ficticios de edad (años) y frecuencia cardíaca (latidos por minuto)
data = {
    'Edad': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'FrecuenciaCardiaca': [80, 78, 75, 72, 70, 68, 65, 63, 60, 58]
}
df = pd.DataFrame(data)
X = df[['Edad']]  # Variable independiente (input)
Y = df['FrecuenciaCardiaca']  # Variable dependiente (output)

modelo = LinearRegression()
modelo.fit(X, Y)
print(f"Intercepto (β₀): {modelo.intercept_}")

valor_predecir = 50
prediccion = modelo.predict([[valor_predecir]])
print(f"Predicción para {valor_predecir} años: {prediccion[0]} latidos por minuto")
# Visualización
plt.scatter(X, Y, color='blue', label='Datos Reales')
plt.plot(X, modelo.predict(X), color='red', label='Regresión Lineal')
plt.scatter(valor_predecir, prediccion, color='green', label='Predicción')
plt.xlabel('Edad (años)')
plt.ylabel('Frecuencia Cardíaca (lpm)')
plt.title('Regresión Lineal: Edad vs Frecuencia Cardíaca')
plt.legend()
plt.grid()
plt.show()

root = tk.Tk()
root.withdraw()  # Oculta la ventana principal
messagebox.showinfo("Análisis", "La relación entre los datos simulados de edad y frecuencia cardíaca es negativa, lo que indica que a medida que aumenta la edad, la frecuencia cardíaca tiende a disminuir.")
