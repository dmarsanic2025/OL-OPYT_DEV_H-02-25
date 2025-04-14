class Sirovina:
    def __init__(self, naziv, dobavljac, kolicina_na_skladistu):
        self.naziv = naziv
        self.dobavljac = dobavljac
        self.kolicina_na_skladistu = kolicina_na_skladistu

    def prikazi_podatke(self):
        print(f"Naziv sirovine: {self.naziv}")
        print(f"Dobavljač: {self.dobavljac}")
        print(f"Količina na skladištu: {self.kolicina_na_skladistu}")


sirovina1 = Sirovina("Aluminij", "AluTrade d.o.o.", 200)
sirovina1.prikazi_podatke()
