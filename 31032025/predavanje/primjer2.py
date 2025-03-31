def funkcija():
    lok_var = "Ja sam lokalna"
    print(lok_var)


def funkcija2():
    lok_var = "Ja sam lokalna2"
    if type(lok_var) == str:
        return lok_var
        print(lok_var)  # ovo se ignorira jer je 'iza' returna
    else:
        print(lok_var)
        return None


funkcija()
print(funkcija2())

print("*" * 70)

globalna_v = "Ja sam globalna"


def moja_f():
    print(globalna_v)


moja_f()
print("*" * 70)


def promijeni_globalnu():
    k = 1
    global globalna_v
    globalna_v = globalna_v + " s"
    print(globalna_v)
    print(k)


k = 0
print(k)
promijeni_globalnu()
print(k)
print(globalna_v)
