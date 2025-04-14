"""
Zadatak 5. Definirajte named tuple Narudžba s poljima kupac,
proizvodi i ukupna cijena. Kreirajte nekoliko instanci named
 tuple Proizvod i instancu named tuple Kupac. Kreirajte instancu
named tuple Narudžba koja sadrži listu proizvoda i izračunatu
ukupnu cijenu. Ispišite sve detalje narudžbe
"""

from collections import namedtuple

Narudzba = namedtuple("Narudžbna", {"kupac", "proizvodi", "ukupna_cijena"})
Kupac = namedtuple("Kupac", {"ime", "prezime"})
Proizvod = namedtuple("Proizvod", {"naziv", "cijena"})

kupac1 = Kupac(ime="David", prezime="Horvat")

Proizvod1 = Proizvod(naziv="Brašno", cijena=10)
Proizvod2 = Proizvod(naziv="Šećer", cijena=5)

lista_proizvoda = [Proizvod1, Proizvod2]

ukupna_cijena = sum(proizvod.cijena for proizvod in lista_proizvoda)

narudzba1 = Narudzba(
    kupac=kupac1, proizvodi=lista_proizvoda, ukupna_cijena=ukupna_cijena
)


for proizvod in narudzba1.proizvodi:
    print(f"{proizvod.naziv} {proizvod.cijena} €")
print(f"Ukupna cijena: {narudzba1.ukupna_cijena} €")
