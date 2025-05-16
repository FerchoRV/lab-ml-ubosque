import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos de ejemplo: metros cuadrados (X) y precios (y)
X = [[50], [60], [70], [80], [90], [100]]
y = [150000, 180000, 210000, 240000, 270000, 300000]

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(X, y)

# Predecir el precio de una casa de 85 m²
prediccion = modelo.predict([[85]])
print(f"El precio estimado para una casa de 85 m² es: ${prediccion[0]:,.2f}")

# Visualizar los datos y la recta de regresión
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, modelo.predict(X), color='red', label='Línea de regresión')
plt.xlabel('Metros cuadrados')
plt.ylabel('Precio')
plt.title('Regresión Lineal: Precio vs Tamaño de la casa')
plt.legend()
plt.grid(True)
plt.show()