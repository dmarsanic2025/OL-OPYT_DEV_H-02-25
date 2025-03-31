studenti = ["Ivan", "Marko", "Ana"]
ocjene = [5, 3]
najdrazi_predmeti = ["Matematika", "Fizika", "Kemija"]

kombinacija = zip(studenti, ocjene)

print(list(kombinacija))

for student, ocjena, predmet in zip(studenti, ocjene, najdrazi_predmeti):
    print(student, ocjena, predmet)
