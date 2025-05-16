#2. Conversión de tipos Enunciado: Pide un número decimal al usuario y conviértelo a entero y cadena. Muestra los resultados y los tipos.

while True:

    dato_user = ((input("Introduce un número decimal: ")))

    if dato_user.isnumeric() == False:
        try:
            dato_user = float(dato_user)
        except ValueError:
            print("El valor introducido no es un número decimal válido.")
            continue

    if type(dato_user) == str or type(dato_user) == int:
        print("El valor introducido no es un número decimal válido.")
    else:
        dato_entero = int(float(dato_user))
        dato_cadena = str(dato_user)

        print(f"El número decimal introducido es: {dato_user} y su tipo es: {type(dato_user)}")
        print(f"El número transformado entero es: {dato_entero} y su tipo es: {type(dato_entero)}")
        print(f"El número tranfromado en cadena es: {dato_cadena} y su tipo es: {type(dato_cadena)}")

        break
