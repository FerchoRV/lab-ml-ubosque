#19. Actualizar valor en diccionario Enunciado: Modifica la edad del estudiante del ejercicio anterior y agrega una nueva clave: "nota final".

estudiante= {
    "nombre": "Ana",
    "edad": 20,
    "curso": "Python"
}
print("Datos originales")
print(estudiante)

estudiante["edad"] = 21
estudiante["nota final"] = 9

print("Datos actualizados")
print(estudiante)