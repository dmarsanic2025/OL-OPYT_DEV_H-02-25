"""
Napravite aplikaciju za prikaz tablice množenja. Korisnik treba moći unijeti do kojeg broja će se prikazati tablica.

"""

while True:

    if input("Zelite li zavrsiti program? (da/ne) ").lower() == "da":
        break
    n = int(input("Unesi broj: "))

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i *j}", sep="\t", end=" ")
        print()
