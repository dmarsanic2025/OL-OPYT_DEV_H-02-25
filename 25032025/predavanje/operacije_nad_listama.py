brojevi = list()  # ili []
for broj in range(20 + 1):
    brojevi.append(broj)

print()
print("Ispis CIJELE LISTE")
for broj in brojevi:
    print(broj, end=" ")
print("\n")

brojevi.clear()
print("Ispis CIJELE LISTE nakon naredbe clear()")
for broj in brojevi:
    print(broj, end=" ")
print("\n")

brojevi = list()  # ili []
for broj in range(20 + 1):
    brojevi.append(broj)

"""
brojevi2 = brojevi
brojevi2.append(25)
brojevi.append(30)
print(brojevi)
print(brojevi2)
"""

brojevi_kopija = brojevi.copy()
print("Ispis brojevi nakon naredbe copy() i nakon naredbe append")
brojevi.append(15)
for broj in brojevi:
    print(broj, end=" ")
print("\n")

print("Ispis brojevi_kopija nakon naredbe copy() i nakon naredbe append")
brojevi_kopija.append(25)
for broj in brojevi_kopija:
    print(broj, end=" ")
print("\n")


trazeni_broj = 15
brojevi_count = brojevi.count(trazeni_broj)
print(f"Broj ponavljanja broja {trazeni_broj} u listi je {brojevi_count}.")
print("\n")

rijeci = ["Python", "Algebra", "Programiranje"]
print("ispis rijeci PRIJE naredbe extend()")
for r in rijeci:
    print(r, end=" ")
print("\n")

rijeci.extend(["Volim", "Jako", "programirat"])
print("ispis rijeci NAKON naredbe extend()")
for r in rijeci:
    print(r, end=" ")
print("\n")


rijeci.extend(brojevi)
print("ispis rijeci NAKON naredbe extend() sa listom brojeva")
for r in rijeci:
    print(r, end=" ")
print("\n")


trazeni_element = "Python"
rijeci_index = rijeci.index(trazeni_element)
print(f"Index za vrijednost {trazeni_element} je {rijeci_index}.")
trazeni_element = 15
rijeci_index = rijeci.index(trazeni_element)
print(f"Index za vrijednost {trazeni_element} je {rijeci_index}.")

rijeci.insert(rijeci_index, "Ispred 15")
print(rijeci)

print("*" * 50)

print("Ispis liste brojevi uz funkciju reversed()")
for broj in reversed(brojevi):
    print(broj, end=" ")
print("\n ")
for broj in brojevi:
    print(broj, end=" ")
print("\n ")

print("Ispis liste brojevi uz funkciju sorted()")
nova_lista = sorted(brojevi, reverse=True)
for broj in nova_lista:
    print(broj, end=" ")
print("\n ")
for broj in brojevi:
    print(broj, end=" ")
print("\n ")

nova_lista2 = brojevi.reverse()
for broj in nova_lista2:
    print(broj, end=" ")
print("\n ")

brojevi.sort(reverse=True)
for broj in brojevi:
    print(broj, end=" ")
print("\n ")
