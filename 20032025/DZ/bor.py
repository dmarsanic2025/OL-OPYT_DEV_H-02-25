"""
Kreirati aplikaciju koja će u konzolu iscrtati bor kao na slici ispod. Korisnik treba unijeti visinu bora i znak.
Primjer ispisa bora za visinu 7 i znak „*“:
      * 1
     ** 2
    **** 4
   ****** 6
  ******** 8
 ********** 10
************ 12
    |||
    |||
"""

visina = int(input("Unesite visinu bora: "))  # visina = 7
znak = input("Unesite znak za iscrtavanje: ")


for i in range(1, visina + 1):
    print(" " * (visina - i) + znak * (2 * i - 1))

for i in range(visina // 2):
    print(" " * (visina - 2) + "|||")
