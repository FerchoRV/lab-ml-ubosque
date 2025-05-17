#23. Leer un archivo de texto Enunciado: Lee el contenido de resumen.txt y muéstralo en consola.

path_documento = "./datos/resumen.txt"

# Leer el contenido del archivo
with open(path_documento, "r") as archivo:
    contenido = archivo.read()

print(f"El contenido del archivo {path_documento} es:\n{contenido}")