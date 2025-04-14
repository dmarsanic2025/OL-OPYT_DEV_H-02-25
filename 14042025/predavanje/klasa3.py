class Korisnik:
    def __init__(self, ime, prezime, email):
        self.ime = ime
        self.prezime = prezime
        self.email = email

    def prikazi_podatke(self):
        print(f"Ime: {self.ime}")
        print(f"Prezime: {self.prezime}")
        print(f"Email: {self.email}")


class Kupac(Korisnik):
    def __init__(self, ime, prezime, email, adresa):
        super().__init__(ime, prezime, email)
        self.adresa = adresa

    def prikazi_podatke(self):
        super().prikazi_podatke()
        print(f"Adresa: {self.adresa}")


kupac1 = Kupac("Ana", "Kovač", "ana@example.com", "Zagrebačka 12, Zagreb")
kupac1.prikazi_podatke()
