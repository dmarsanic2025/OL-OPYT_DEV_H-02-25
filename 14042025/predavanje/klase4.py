class Usluga:
    def __init__(self, naziv, cijena_po_satu):
        self.naziv = naziv
        self.cijena_po_satu = cijena_po_satu

    def prikazi_podatke(self):
        print(f"Usluga: {self.naziv}")
        print(f"Cijena po satu: {self.cijena_po_satu} EUR")


class GrafickaUsluga(Usluga):
    def __init__(self, naziv, cijena_po_satu, vrijeme_izrade):
        super().__init__(naziv, cijena_po_satu)
        self.vrijeme_izrade = vrijeme_izrade

    def prikazi_podatke(self):
        super().prikazi_podatke()
        print(f"Vrijeme izrade: {self.vrijeme_izrade} sati")


usluga1 = GrafickaUsluga("Dizajn logotipa", 30, 5)
usluga1.prikazi_podatke()
