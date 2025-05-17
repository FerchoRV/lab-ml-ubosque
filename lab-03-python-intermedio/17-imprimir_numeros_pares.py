#17. Imprimir solo números pares del 1 al 20 Enunciado: Usa un ciclo for para imprimir solo los números pares entre 1 y 20.

contador = 0
for contador in range(1, 21):
    if contador % 2 == 0:
        print(contador)
        