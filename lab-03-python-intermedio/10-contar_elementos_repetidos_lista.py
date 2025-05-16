#10. Contar elementos en una lista Enunciado: Crea una lista de frutas y cuenta cuántas veces aparece una fruta específica.

lista_frutas = ["manzana", "pera","manzana"]

fruta_a_contar = "manzana"
contador = 0

for fruta in lista_frutas:
    if fruta == fruta_a_contar:
        contador += 1

print(f"La fruta '{fruta_a_contar}' aparece {contador} veces en la lista.")