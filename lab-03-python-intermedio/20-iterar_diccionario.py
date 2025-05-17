#20. Iterar sobre un diccionario Enunciado: Imprime todas las claves y valores del diccionario anterior.

estudiante= {
    "nombre": "Ana",
    "edad": 20,
    "curso": "Python"
}

estudiante["edad"] = 21
estudiante["nota final"] = 9

for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")