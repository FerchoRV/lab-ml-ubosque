#14. Suma acumulada con while Enunciado: Pide números hasta que el usuario escriba 0. Luego muestra la suma total.

numero_user = int(input("Introduce un número (0 para salir): "))

lista_numeros= []

while numero_user != 0:
    lista_numeros.append((numero_user))
    numero_user = int(input("Introduce un número (0 para salir): "))

suma_total = sum(lista_numeros)
print(f"La suma total es: {suma_total}")