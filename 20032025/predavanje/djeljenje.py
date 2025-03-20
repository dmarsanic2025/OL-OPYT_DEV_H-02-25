for broj in range(1, 31):
    if broj % 3 == 0:
        print(f"Broj {broj} je djeljiv s 3")
    elif broj % 6 == 0:
        print(f"Broj {broj} je djeljiv sa 6")
    elif broj % 9 == 0:
        print(f"Broj {broj} je djeljiv s 9")
    else:
        print(f"Broj {broj} NIJE djeljiv s 3, 6 ili 9")

print("*" * 30)
for broj in range(1, 31):
    if broj % (3 * 3) == 0:
        print(f"Broj {broj} je djeljiv s 9")

    if broj % (3 * 2) == 0:
        print(f"Broj {broj} je djeljiv sa 6")

    if broj % 3 == 0:
        print(f"Broj {broj} je djeljiv s 3")
    else:
        print(f"Broj {broj} NIJE djeljiv s 3, 6 ili 9")
