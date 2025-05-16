import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos de entrada
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Crear y entrenar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Generar datos para dibujar la línea
X_linea = np.linspace(1, 6, 100).reshape(-1, 1)  # Corregido: X_linea en lugar de x_linea
y_pred = modelo.predict(X_linea)

# Graficar
plt.scatter(X, y, color="blue", label="Datos originales")
plt.plot(X_linea, y_pred, color="red", label="Modelo")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Regresión Lineal Simple")
plt.legend()
plt.grid()
plt.show()