class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

    def prikazi_podatke(self):
        print(f"{self.ime} {self.prezime}")


class Student(Osoba):
    def __init__(self, ime, prezime, broj_indeksa):
        super().__init__(ime, prezime)
        self.broj_indeksa = broj_indeksa

    def prikazi_podatke(self):
        super().prikazi_podatke()
        print(f"Broj indeksa: {self.broj_indeksa}")


student = Student("Ivan", "Horvat", "52423423")
student.prikazi_podatke()
