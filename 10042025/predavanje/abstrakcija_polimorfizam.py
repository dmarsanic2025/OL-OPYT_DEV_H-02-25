from abc import ABC, abstractmethod


# 1 zadatak sa slajda
class Vozilo(ABC):
    @abstractmethod
    def pokreni_motor(self):
        pass


class Automobil(Vozilo):
    def pokreni_motor(self):
        print("Sjedanje za volan, pokreće se START/STOP!")


class Motocikl(Vozilo):
    def pokreni_motor(self):
        print("Sjedanje na motor, okretanje ključa i spuštanje desne ručice.")


def pokreni_motor_ispis(vozilo: Automobil | Motocikl):
    vozilo.pokreni_motor()


automobil = Automobil()
motocikl = Motocikl()

pokreni_motor_ispis(automobil)
pokreni_motor_ispis(motocikl)
