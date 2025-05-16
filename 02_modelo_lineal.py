from sklearn.linear_model import LinearRegression
import numpy as np

# Datos de entrada
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Predecir nuevos valores
nuevos_datos = np.array([[6], [7]])
predicciones = modelo.predict(nuevos_datos)

print("Predicciones:", predicciones)