prazan_set = set()  # nikako {}
brojevi = {1, 2, 3, 4, 5}
print(brojevi)


duplici = {11, 1, 1, 1, 22, 33, 4, 4, 4, "5", 5, False, 5.0}
print(duplici)

a = {1, 2, 3, 4}
b = {4, 3, 5, 6}

unija = a | b
print(unija)

presjek = a & b
print(presjek)


razlika = a - b
print(razlika)

simetricna_razlika = a ^ b
print(simetricna_razlika)


duplici.add(555)
print(duplici)
duplici.update([444, 666, 777])
print(duplici)
duplici.discard(False)
print(duplici)
duplici.remove("5")
print(duplici)

if 22 in duplici:
    print("22 se nalazi u duplicima")

ovo_je_neka_lista = [1, 2, 3, 4, 5, 5, 5, 5, 1, 2, 3, 4, 5, 5, 5]

ovo_je_neki_set = set(ovo_je_neka_lista)
print(ovo_je_neki_set)
