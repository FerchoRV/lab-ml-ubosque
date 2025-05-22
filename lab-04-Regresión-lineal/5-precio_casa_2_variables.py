# Ejercicio 5
# Agrega una segunda variable al ejercicio anterior: número de habitaciones. Usa regresión lineal múltiple para
# predecir el precio.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos ficticios de metros cuadrados, número de habitaciones y precios de casas
data = {
    'MetrosCuadrados': [50, 60, 70, 80, 90, 100, 110, 120],
    'NumeroHabitaciones': [1, 2, 2, 3, 3, 4, 4, 5],
    'PrecioCasa': [150000, 180000, 210000, 240000, 270000, 300000, 330000, 360000]
}
df = pd.DataFrame(data)
X = df[['MetrosCuadrados', 'NumeroHabitaciones']]  # Variables independientes (input)
Y = df['PrecioCasa']  # Variable dependiente (output)
modelo = LinearRegression()
modelo.fit(X, Y)
print(f"Intercepto (β₀): {modelo.intercept_}")
valor_predecir = np.array([[130, 3]])  # 130 m² y 3 habitaciones
prediccion = modelo.predict(valor_predecir)
print(f"Predicción para {valor_predecir[0][0]} m² y {valor_predecir[0][1]} habitaciones: {prediccion[0]} €")

# Visualización
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['MetrosCuadrados'], df['NumeroHabitaciones'], df['PrecioCasa'], color='blue', label='Datos Reales')
ax.set_xlabel('Metros Cuadrados')
ax.set_ylabel('Número de Habitaciones')
ax.set_zlabel('Precio Casa (€)')

# Crear una malla de puntos para la superficie de regresión
x_surf, y_surf = np.meshgrid(np.linspace(df['MetrosCuadrados'].min(), df['MetrosCuadrados'].max(), 10),
                             np.linspace(df['NumeroHabitaciones'].min(), df['NumeroHabitaciones'].max(), 10))
z_surf = modelo.predict(np.c_[x_surf.ravel(), y_surf.ravel()])
z_surf = z_surf.reshape(x_surf.shape)
ax.plot_surface(x_surf, y_surf, z_surf, color='red', alpha=0.5, label='Regresión Lineal')
ax.scatter(valor_predecir[0][0], valor_predecir[0][1], prediccion, color='green', label='Predicción')
ax.legend()
plt.title('Regresión Lineal Múltiple: Metros Cuadrados y Habitaciones vs Precio Casa')
plt.show()

#Visualización 2D
plt.scatter(df['MetrosCuadrados'], df['PrecioCasa'], color='blue', label='Datos Reales')
plt.scatter(df['NumeroHabitaciones'], df['PrecioCasa'], color='orange', label='Datos Reales')
plt.plot(df['MetrosCuadrados'], modelo.predict(X), color='red', label='Regresión Lineal')
plt.scatter(valor_predecir[0][0], prediccion, color='green', label='Predicción')
plt.xlabel('Metros Cuadrados y Número de Habitaciones')
plt.ylabel('Precio Casa (€)')
plt.title('Regresión Lineal Múltiple: Metros Cuadrados y Habitaciones vs Precio Casa')
plt.legend()
plt.grid()
plt.show()
