# lambda arguments: expression
zbroji = lambda x, y: x + y
print(zbroji(5, 3))

je_li_paran = lambda x: x % 2 == 0
print(je_li_paran(55))
print(je_li_paran(552))

print("*" * 70)


brojevi = [1, 2, 3, 4, 5, 6]
parbni_brojevi = list(filter(lambda x: x % 2 == 0, brojevi))

# ili


def paran(x):
    return x % 2 == 0


parbni_brojevi2 = list(filter(paran, brojevi))
print(parbni_brojevi2)
print(paran(5))


def implementacija_filter(funkcija, lista):
    nova_lista = []
    for element in lista:
        if funkcija(element) == True:
            nova_lista.append(element)
    return nova_lista


def implementacija_filter_list_comperhension(funkcija, lista):
    return [element for element in lista if funkcija(element)]


print(implementacija_filter(paran, brojevi))
