# Ejercicio 6
# Usa datos de velocidad del viento (km/h) y rendimiento de una turbina eólica. Entrena una regresión y grafica
# los resultados.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos ficticios de velocidad del viento (km/h) y rendimiento de una turbina eólica (kWh)
data = {
    'VelocidadViento': [5, 10, 15, 20, 25, 30, 35, 40],
    'RendimientoTurbina': [100, 200, 300, 400, 500, 600, 700, 800]
}

df = pd.DataFrame(data)
X = df[['VelocidadViento']]  # Variable independiente (input)
Y = df['RendimientoTurbina']  # Variable dependiente (output)
modelo = LinearRegression()
modelo.fit(X, Y)
print(f"Intercepto (β₀): {modelo.intercept_}")
valor_predecir = 45
prediccion = modelo.predict([[valor_predecir]])
print(f"Predicción para {valor_predecir} km/h: {prediccion[0]} kWh")
# Visualización
plt.scatter(X, Y, color='blue', label='Datos Reales')
plt.plot(X, modelo.predict(X), color='red', label='Regresión Lineal')
plt.scatter(valor_predecir, prediccion, color='green', label='Predicción')
plt.xlabel('Velocidad del Viento (km/h)')   
plt.ylabel('Rendimiento de la Turbina (kWh)')
plt.title('Regresión Lineal: Velocidad del Viento vs Rendimiento de la Turbina')
plt.legend()
plt.grid()
plt.show()
