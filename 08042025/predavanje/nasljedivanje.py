class Nadklasa:
    def __init__(self, atribut1):
        self.atribut1 = atribut1

    def metoda1(self):
        print("Ovo je metoda nadklase.")


class PodKlasa(Nadklasa):
    def __init__(self, atribut1, atribut2):
        # super().__init__(atribut1)
        # ILI
        Nadklasa.__init__(self, atribut1)
        self.atribut2 = atribut2

    def metoda2(self):
        print("Ovo je metoda podklase.")


nadklasa_objekt = Nadklasa("Vozilo")
nadklasa_objekt.metoda1()
# nadklasa_objekt.metoda2() ne radi
podklasa_objekt = PodKlasa("Vozilo", "Automobil")
podklasa_objekt.metoda1()
podklasa_objekt.metoda2()
print(nadklasa_objekt.atribut1)
print(podklasa_objekt.atribut1)
print(podklasa_objekt.atribut2)
