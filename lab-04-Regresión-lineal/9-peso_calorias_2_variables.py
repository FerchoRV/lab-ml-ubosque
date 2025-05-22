# Ejercicio 9
# Agrega al ejercicio 8 una segunda variable: nivel de actividad física (de 1 a 5). Realiza una regresión lineal
# múltiple.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos ficticios de peso (kg), calorías y nivel de actividad física
datos = {
    'Peso': [50, 55, 60, 65, 70, 75, 80, 85],
    'Calorias': [2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400],
    'NivelActividad': [1, 2, 3, 4, 5, 1, 2, 3]
}
df = pd.DataFrame(datos)
X = df[['Peso', 'NivelActividad']]  # Variables independientes (input)
Y = df['Calorias']  # Variable dependiente (output)
modelo = LinearRegression()
modelo.fit(X, Y)
print(f"Intercepto (β₀): {modelo.intercept_}")
valor_predecir = [90, 4]  # Peso y nivel de actividad
prediccion = modelo.predict([valor_predecir])
print(f"Predicción para {valor_predecir[0]} kg y nivel de actividad {valor_predecir[1]}: {prediccion[0]} calorías")

# Visualización 3D con superficie de regresión
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Peso'], df['NivelActividad'], df['Calorias'], color='blue', label='Datos Reales')
ax.set_xlabel('Peso (kg)')
ax.set_ylabel('Nivel de Actividad')
ax.set_zlabel('Calorías')

# Crear una malla de puntos para la superficie de regresión
x_surf, y_surf = np.meshgrid(
    np.linspace(df['Peso'].min(), df['Peso'].max(), 10),
    np.linspace(df['NivelActividad'].min(), df['NivelActividad'].max(), 10)
)
z_surf = modelo.predict(np.c_[x_surf.ravel(), y_surf.ravel()])
z_surf = z_surf.reshape(x_surf.shape)
ax.plot_surface(x_surf, y_surf, z_surf, color='red', alpha=0.5)

# Mostrar la predicción
ax.scatter(valor_predecir[0], valor_predecir[1], prediccion, color='green', label='Predicción')
ax.legend()
plt.title('Regresión Lineal Múltiple: Peso y Nivel de Actividad vs Calorías')
plt.show()


# Visualización 2D (Peso y Nivel de Actividad vs Calorías)
plt.scatter(df['Peso'], df['Calorias'], color='blue', label='Peso vs Calorías')
plt.scatter(df['NivelActividad'], df['Calorias'], color='orange', label='NivelActividad vs Calorías')
plt.plot(df['Peso'], modelo.predict(X), color='red', label='Regresión Lineal')
plt.scatter(valor_predecir[0], prediccion, color='green', label='Predicción')
plt.xlabel('Peso (kg) y Nivel de Actividad')
plt.ylabel('Calorías')
plt.title('Regresión Lineal Múltiple: Peso y Nivel de Actividad vs Calorías')
plt.legend()
plt.grid()
plt.show()