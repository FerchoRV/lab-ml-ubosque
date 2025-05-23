import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# Cargar el dataset de cáncer de mama
cancer = load_breast_cancer()
# Convertir a DataFrame
cancer_df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
# Añadir la variable objetivo
cancer_df['target'] = cancer.target
# Mostrar las primeras filas del DataFrame
print(cancer_df.head(3))

# Dividir el dataset en características y variable objetivo
X = cancer_df.drop('target', axis=1)
y = cancer_df['target']
# Dividir el dataset en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Crear el modelo de regresión logística
model = LogisticRegression(max_iter=10000)
# Entrenar el modelo
model.fit(X_train, y_train)
# Hacer predicciones
y_pred = model.predict(X_test)
# Calcular la matriz de confusión
cm = confusion_matrix(y_test, y_pred)

# Graficar la matriz de confusión
plt.figure(figsize=(8, 6))
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Matriz de Confusión')
plt.colorbar()
tick_marks = np.arange(2)
plt.xticks(tick_marks, ['Maligno', 'Benigno'])
plt.yticks(tick_marks, ['Maligno', 'Benigno'])

# Mostrar los valores dentro de la matriz
thresh = cm.max() / 2.
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, format(cm[i, j], 'd'),
                 ha="center", va="center",
                 color="white" if cm[i, j] > thresh else "black")

plt.ylabel('Etiqueta verdadera')
plt.xlabel('Etiqueta predicha')
plt.tight_layout()
plt.show()