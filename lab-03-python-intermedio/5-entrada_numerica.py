#5. Entrada numérica Enunciado: Solicita al usuario su edad y muéstrala como número entero, flotante y cadena.
while True:
    edad_user = input("Ingresa tu edad: ")
    if not edad_user.isdigit():
        print("Por favor, ingresa solo números enteros válidos.")
        continue
    edad_entero = int(edad_user)
    edad_float = float(edad_entero)
    edad_cadena = str(edad_entero)

    print(f"El número entero introducido es: {edad_entero} y su tipo es: {type(edad_entero)}")
    print(f"El número transformado a flotante es: {edad_float} y su tipo es: {type(edad_float)}")
    print(f"El número transformado en cadena es: {edad_cadena} y su tipo es: {type(edad_cadena)}")
    break
