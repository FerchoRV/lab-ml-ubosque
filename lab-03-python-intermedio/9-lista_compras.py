#9. Lista de compras Enunciado: Crea una lista de compras, añade 3 productos, elimina 1 y muestra la lista final.

lista_compras =[]

lista_compras.append("pan")
lista_compras.append("leche")
lista_compras.append("huevos")

lista_compras.remove("leche")

print("Lista de compras final:")
for producto in lista_compras:
    print(producto)
