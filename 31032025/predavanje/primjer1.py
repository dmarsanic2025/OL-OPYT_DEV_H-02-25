def ispisi(tekst: str) -> None:
    print(tekst)


def ispisi2(tekst: str) -> None:
    print(tekst)
    return None


def kvadrat(x: int | float) -> int | float:
    return x * x


povratna_v = ispisi("Bok")
print(povratna_v)

povratna_v = ispisi2("Bok")
print(povratna_v)

povratna_v2 = kvadrat(5)
print(povratna_v2)
