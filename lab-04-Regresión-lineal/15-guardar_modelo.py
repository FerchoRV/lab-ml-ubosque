# Ejercicio 15
# Guarda el modelo entrenado con joblib y luego cárgalo para hacer predicciones con nuevos datos.

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import numpy as np
import matplotlib.pyplot as plt

path_modelo = './modelos/15-modelo_regresion_lineal.pkl'
# simular datos de notas de estudiantes
np.random.seed(0)
X = np.random.rand(100, 1) * 10  # horas de estudio
y = 2 * X + np.random.randn(100, 1) * 2  # notas con algo de ruido
# crear un DataFrame
data = pd.DataFrame(data=np.hstack((X, y)), columns=['HorasEstudio', 'Notas'])

print(data.head(3))
# dividir el dataset en características y variable objetivo
X = data[['HorasEstudio']]
y = data['Notas']
# Entrenar el modelo
model = LinearRegression()
model.fit(X, y)

#guardar el modelo
joblib.dump(model, path_modelo)
#cargar el modelo
loaded_model = joblib.load(path_modelo)
# hacer predicciones con el modelo cargado
valor_prediccion = float(input("Introduce el número de horas de estudio: "))
X_nuevo = np.array([[valor_prediccion]])
y_prediccion = loaded_model.predict(X_nuevo)
print(f"Predicción de la nota para {valor_prediccion} horas de estudio: {y_prediccion[0]:.2f}")