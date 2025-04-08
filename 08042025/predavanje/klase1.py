class Automobil:
    def __init__(self, marka, model, godina):
        self.marka = marka
        self.model = model
        self.year = godina

    def ispis_info(self):
        print(self.marka, self.model, self.year)


auto = Automobil("Opel", "Astra", 2000)
print(auto.marka, auto.model, auto.year)

auto.ispis_info()
