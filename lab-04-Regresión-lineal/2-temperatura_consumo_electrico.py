# Ejercicio 2
# Utiliza datos de temperatura (°C) y consumo eléctrico (kWh). Ajusta una regresión lineal y predice el
# consumo para 35°C.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos de temperatura (°C) y consumo eléctrico (kWh)
data = {
    'Temperatura': [20, 22, 24, 26, 28, 30, 32, 34],
    'ConsumoElectrico': [150, 160, 170, 180, 190, 200, 210, 220]
}
df = pd.DataFrame(data)
X = df[['Temperatura']]  # Variable independiente (input)
Y = df['ConsumoElectrico']  # Variable dependiente (output)
modelo = LinearRegression()
modelo.fit(X, Y)

print(f"Intercepto (β₀): {modelo.intercept_}")
valor_predecir = 35
prediccion = modelo.predict([[valor_predecir]])
print(f"Predicción para {valor_predecir}°C: {prediccion[0]} kWh")
# Visualización
plt.scatter(X, Y, color='blue', label='Datos Reales')
plt.plot(X, modelo.predict(X), color='red', label='Regresión Lineal')
plt.scatter(valor_predecir, prediccion, color='green', label='Predicción')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Consumo Eléctrico (kWh)')
plt.title('Regresión Lineal: Temperatura vs Consumo Eléctrico')
plt.legend()
plt.grid()
plt.show()