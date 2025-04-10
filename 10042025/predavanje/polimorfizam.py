class Zivotinja:
    def napravi_zvuk(self):
        pass


class Pas(Zivotinja):
    def napravi_zvuk(self):
        print("Vau!")


class Macka(Zivotinja):
    def napravi_zvuk(self):
        print("Mijau!")


def ispisi_zvuk(zivotinja: Pas | Macka):
    zivotinja.napravi_zvuk()


pas = Pas()
macka = Macka()

ispisi_zvuk(pas)
ispisi_zvuk(macka)
