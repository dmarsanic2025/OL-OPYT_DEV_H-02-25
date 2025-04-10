from collections import namedtuple

Osoba = namedtuple("Osoba", ["ime", "prezime", "godine"])

osoba1 = Osoba(ime="Ivan", prezime="Horvat", godine=10)
osoba2 = Osoba(ime="Pero", prezime="Peric", godine=100)

print(osoba1.godine)
print(osoba1.prezime)
print(osoba1.ime)


print(osoba2._fields)

osoba3 = osoba1._replace(godine=31, prezime="Bok")
print(osoba3.godine)
print(osoba3.prezime)
print(osoba1.godine)

osoba_dict = osoba1._asdict()
print(osoba_dict)
