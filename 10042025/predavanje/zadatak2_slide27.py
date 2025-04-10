"""
Zadatak 2. Definirajte namedtuple Sirovina s poljima naziv,
dobavljač i količina na skladištu. Kreirajte listu nekoliko instanci
named tuple Sirovina. Ispišite informacije o svim sirovinama u
listi.
"""

from collections import namedtuple

Sirovina = namedtuple("Sirovina", ["naziv", "dobavljac", "kolicina_na_skladistu"])

sirovine = [
    Sirovina("Metal", "Metalni d.o.o", 500),
    Sirovina("Zlato", "Zlatni d.o.o", 1),
    Sirovina("Plastika", "Plasticni d.o.o", 52),
]

print("\nSirovine:")

for sirovina in sirovine:
    print(
        f"Naziv: {sirovina.naziv}, Dobavljač: {sirovina.dobavljac}, Količina: {sirovina.kolicina_na_skladistu}"
    )
