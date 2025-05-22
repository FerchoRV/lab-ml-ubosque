# Ejercicio 1
# Crea un conjunto de datos con los años de experiencia y salario de 10 empleados. Aplica regresión lineal para
# predecir el salario.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    'AniosExperiencia': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salario': [30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000]
}


df = pd.DataFrame(data)

X = df[['AniosExperiencia']]  # Variable independiente (input)

Y = df['Salario']             # Variable dependiente (output)

modelo = LinearRegression()
modelo.fit(X, Y)

print(f"Intercepto (β₀): {modelo.intercept_}")

valor_predecir = 11
prediccion = modelo.predict([[valor_predecir]])
print(f"Predicción para {valor_predecir} años de experiencia: {prediccion[0]}")

# Visualización
plt.scatter(X, Y, color='blue', label='Datos Reales')
plt.plot(X, modelo.predict(X), color='red', label='Regresión Lineal')
plt.scatter(valor_predecir, prediccion, color='green', label='Predicción')
plt.xlabel('Años de Experiencia')
plt.ylabel('Salario')
plt.title('Regresión Lineal: Años de Experiencia vs Salario')
plt.legend()
plt.grid()
plt.show()
