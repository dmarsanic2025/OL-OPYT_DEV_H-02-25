"""
Zadatak 7. Definirajte klasu Korisnik s atributima ime i email. Kreirajte metodu
prikazi_podatke koja ispisuje podatke o korisniku. Definirajte podklasu
 Prodavač koja nasljeđuje Korisnik i dodaje atribut broj_prodanih_proizvoda.
Nadjačajte metodu prikazi_podatke u podklasi Prodavač. Kreirajte funkciju
prikazi_informacije koja koristi polimorfizam za ispis podataka o korisniku, bilo
da je Korisnik ili Prodavač.
"""


class Korisnik:
    def __init__(self, ime, email):
        self.ime = ime
        self.email = email

    def prikazi_podatke(self):
        print(f"Korisnik: {self.ime}, e-mail: {self.email}")


class Prodavac(Korisnik):
    def __init__(self, ime, email, broj_prodanih_proizvoda):
        super().__init__(ime, email)
        self.broj_prodanih_proizvoda = broj_prodanih_proizvoda

    def prikazi_podatke(self):
        super().prikazi_podatke()
        print(f"Broj prodanih proizvoda: {self.broj_prodanih_proizvoda}")


def prikazi_informacije(korisnik: Korisnik | Prodavac):
    korisnik.prikazi_podatke()


korisnik = Korisnik("Ana", "ana@yahhoooo.com")
prodavac = Prodavac("ivan", "iiivan@hotmail.com", 150)

prikazi_informacije(korisnik)
prikazi_informacije(prodavac)
