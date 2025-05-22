# Ejercicio 3
# Genera un conjunto de datos con el número de horas de estudio y la calificación obtenida en un examen.
# Entrena un modelo y predice la calificación con 6.5 horas de estudio.

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 

# Datos de horas de estudio y calificaciones
data = {
    'HorasEstudio': [1, 2, 3, 4, 5, 6, 7, 8],
    'Calificacion': [20, 30, 40, 50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)

X = df[['HorasEstudio']]  # Variable independiente (input)
Y = df['Calificacion']  # Variable dependiente (output)

modelo = LinearRegression()
modelo.fit(X, Y)

print(f"Intercepto (β₀): {modelo.intercept_}")

valor_predecir = 6.5
prediccion = modelo.predict([[valor_predecir]])
print(f"Predicción para {valor_predecir} horas de estudio: {prediccion[0]} puntos")

# Visualización
plt.scatter(X, Y, color='blue', label='Datos Reales')
plt.plot(X, modelo.predict(X), color='red', label='Regresión Lineal')
plt.scatter(valor_predecir, prediccion, color='green', label='Predicción')
plt.xlabel('Horas de Estudio')
plt.ylabel('Calificación')
plt.title('Regresión Lineal: Horas de Estudio vs Calificación')
plt.legend()
plt.grid()
plt.show()
