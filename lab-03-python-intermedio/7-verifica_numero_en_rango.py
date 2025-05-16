#7. Verifica si un número está en un rango Enunciado: Pide un número y verifica si está entre 10 y 20.

while True:
    numero = (input("Introduce un número entero: "))

    if not numero.isdigit():
        print("El valor ingresado no es un número")
        continue

    numero = float(numero)    
    if 10 <= numero <= 20:
        print("El número está en el rango de 10 a 20")
        break
    else:
        print("El número no está en el rango de 10 a 20")
        break
