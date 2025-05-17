#21. Crear una carpeta Enunciado: Crea una carpeta llamada datos si no existe.

import os

path_carpeta = "./datos"

if not os.path.exists(path_carpeta):
    os.makedirs(path_carpeta)
    print(f"Carpeta '{path_carpeta}' creada con exito.")
else:
    print(f"La carpeta '{path_carpeta}' ya existe.")