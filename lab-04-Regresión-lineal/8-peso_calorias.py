# Ejercicio 8
# Genera un conjunto de datos con el peso (kg) y el consumo diario de calorías. Entrena el modelo y evalúa con
# un gráfico.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

datos = {
    'Peso': [50, 55, 60, 65, 70, 75, 80, 85],
    'Calorias': [2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400]
}
df = pd.DataFrame(datos)
X = df[['Peso']]  # Variable independiente (input)
Y = df['Calorias']  # Variable dependiente (output)
modelo = LinearRegression()
modelo.fit(X, Y)
print(f"Intercepto (β₀): {modelo.intercept_}")
valor_predecir = 90
prediccion = modelo.predict([[valor_predecir]])
print(f"Predicción para {valor_predecir} kg: {prediccion[0]} calorías")
# Visualización
plt.scatter(X, Y, color='blue', label='Datos Reales')
plt.plot(X, modelo.predict(X), color='red', label='Regresión Lineal')
plt.scatter(valor_predecir, prediccion, color='green', label='Predicción')
plt.xlabel('Peso (kg)')
plt.ylabel('Consumo Diario de Calorías')
plt.title('Regresión Lineal: Peso vs Consumo Diario de Calorías')
plt.legend()
plt.grid()
plt.show()
