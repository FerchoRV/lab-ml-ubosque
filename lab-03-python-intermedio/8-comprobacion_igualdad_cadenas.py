# 8. Comprobación de igualdad de cadenas Enunciado: Verifica si dos cadenas ingresadas por el usuario son iguales, ignorando mayúsculas.

cadena_1= input("Introduce la primera cadena: ")
cadena_2= input("Introduce la segunda cadena: ")

if cadena_1.lower() == cadena_2.lower():
    print("Las cadenas son iguales (ignorando mayúsculas).")
else:
    print("Las cadenas son diferentes.")