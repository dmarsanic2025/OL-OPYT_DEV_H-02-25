lista = [154, "tekst", "jos jedan tekst", 3.14, True, "Pa opet tekst"]
prazna_lista = []

prvi_element = lista[0]
drugi_element = lista[1]

print(prvi_element, drugi_element[2], sep="\n")

print(lista[5][1])


brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for broj in range(1, 11):
    print(broj, end=" ")
print()
for broj in brojevi:
    print(broj, end=" ")

print()
print("******")

lista_str = ["tekst1", "jos jedan tekst", "Pa opet tekst"]
for tekst in lista_str:
    for slovo in tekst:
        print(slovo, end="")
    print()

print("******")
for index_liste in range(len(lista_str)):
    for index_teksta in range(len(lista_str[index_liste])):
        print(lista_str[index_liste][index_teksta], end="")
    print()
