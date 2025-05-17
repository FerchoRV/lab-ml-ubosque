#24. Leer archivo Excel Enunciado: Carga un archivo de Excel llamado alumnos.xlsx y muestra las primeras 5 filas.

import pandas as pd

path_excel = "./datos/alumnos.xlsx"

df = pd.read_excel(path_excel)

print(df.head(5))