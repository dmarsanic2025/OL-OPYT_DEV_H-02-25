lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista[:5])

lista[1:5] = [11, 12, 13, 14]
print(lista)

del lista[1:5]
print(lista)

lista2 = lista[::2]
lista.append(1)
lista2.append(2)
print(lista)
print(lista2)
