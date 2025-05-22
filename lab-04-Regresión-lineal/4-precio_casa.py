# Ejercicio 4
# Crea una regresión lineal para predecir el precio de una casa en función de los metros cuadrados. Usa datos
# ficticios.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos ficticios de metros cuadrados y precios de casas
data = {
    'MetrosCuadrados': [50, 60, 70, 80, 90, 100, 110, 120],
    'PrecioCasa': [150000, 180000, 210000, 240000, 270000, 300000, 330000, 360000]
}
df = pd.DataFrame(data)
X = df[['MetrosCuadrados']]  # Variable independiente (input)
Y = df['PrecioCasa']  # Variable dependiente (output)
modelo = LinearRegression()
modelo.fit(X, Y)
print(f"Intercepto (β₀): {modelo.intercept_}")
valor_predecir = 130
prediccion = modelo.predict([[valor_predecir]])
print(f"Predicción para {valor_predecir} m²: {prediccion[0]} €")
# Visualización
plt.scatter(X, Y, color='blue', label='Datos Reales')
plt.plot(X, modelo.predict(X), color='red', label='Regresión Lineal')
plt.scatter(valor_predecir, prediccion, color='green', label='Predicción')
plt.xlabel('Metros Cuadrados')
plt.ylabel('Precio Casa (€)')
plt.title('Regresión Lineal: Metros Cuadrados vs Precio Casa')
plt.legend()
plt.grid()
plt.show()

