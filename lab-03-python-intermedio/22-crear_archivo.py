#22. Crear un archivo dentro de una carpeta Enunciado: Crea un archivo de texto llamado resumen.txt dentro de datos y escribe "Laboratorio de Python".

path_documento = "./datos/resumen.txt"
texto = "Laboratorio de Python"
with open(path_documento, "w") as archivo:
    archivo.write(texto)

print(f"Se ha creado el archivo {path_documento} con el texto: {texto}")