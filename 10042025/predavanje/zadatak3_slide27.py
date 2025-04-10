"""
 Zadatak 3. Definirajte named tuple Kupac s poljima ime,
prezime i adresa. Kreirajte instancu named tuple Kupac i
nadogradite adresu koristeći metodu _replace(). Ispišite
originalnu i novu adresu.

"""

from collections import namedtuple

Kupac = namedtuple("Kupac", ["ime", "prezime", "adresa"])

kupac = Kupac(ime="Pero", prezime="Peric", adresa="Trg bana jelacica 1")

novi_kupac = kupac._replace(adresa="vukovarska 1")

print(kupac.adresa)
print(novi_kupac.adresa)
