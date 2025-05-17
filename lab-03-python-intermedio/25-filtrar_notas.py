#25. Filtrar alumnos con nota mayor a 8 Enunciado: Desde el archivo anterior, filtra e imprime los alumnos con nota superior a 8.

import pandas as pd

path_excel = "./datos/alumnos.xlsx"

df = pd.read_excel(path_excel)

# Filtrar alumnos con nota mayor a 8
df_filtrado = df[df["nota"] > 8]

print("Alumnos con nota mayor a 8:")
print(df_filtrado)