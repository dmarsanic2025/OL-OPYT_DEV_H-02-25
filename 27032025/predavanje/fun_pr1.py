def pozdrav(ime):
    print(f"Pozdrav, {ime}!")
    return None


def zbroji(a: int | float, b: int | float) -> int | float:
    return a + b


pozdrav("Dominik")
pozdrav("Marko")

rezultat = zbroji(b=55.55, a=15)
print("Rezultat zbroja iznosi: ", rezultat)


def ispisi_poruku(poruka="Ovo je jako jako pametna poruka!"):
    print(poruka)


ispisi_poruku("Hello World")
ispisi_poruku("")
ispisi_poruku()
ispisi_poruku(poruka="E, ovo je neka poruka")


def ispisi_listu_stringova(lista_stringova: list[str]) -> None:
    for element in lista_stringova:
        print(element)
