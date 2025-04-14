"""
 • Zadatak 4. Definirajte named tuple Ponuda s poljima proizvod,
količina i ukupna cijena. Kreirajte funkciju izracunaj_ponudu
 koja prima instancu named tuple Proizvod i količinu, te vraća
instancu named tuple Ponuda s izračunatom ukupnom cijenom
(cijena proizvoda * količina).
"""

from collections import namedtuple

Ponuda = namedtuple("Ponuda", ["proizvod", "kolicina", "ukupna_cijena"])
Proizvod = namedtuple("Proizvod", ["naziv", "cijena"])


def izaracunaj_ponudu(proizvod: Proizvod, kolicina: int) -> Ponuda:
    ukupna_cijena = proizvod.cijena * kolicina
    return Ponuda(proizvod=proizvod, kolicina=kolicina, ukupna_cijena=ukupna_cijena)


proizvod1 = Proizvod(naziv="MacBook", cijena=1500)
ponuda = izaracunaj_ponudu(proizvod1, 2)
print(ponuda.ukupna_cijena)
