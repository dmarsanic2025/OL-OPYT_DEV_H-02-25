class Proizvod:
    def __init__(self, naziv, cijena, kolicina_na_skladistu):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina_na_skladistu = kolicina_na_skladistu

    def prikazi_podatke(self):
        print(f"Naziv proizvoda: {self.naziv}")
        print(f"Cijena: {self.cijena} EUR")
        print(f"Količina na skladištu: {self.kolicina_na_skladistu}")


proizvod1 = Proizvod("Laptop", 1200, 5)
proizvod1.prikazi_podatke()
