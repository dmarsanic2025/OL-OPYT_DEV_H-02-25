for slovo in "Python Programer":
    print(slovo, end="")

print()

for slovo in "Python Programer":
    if slovo.lower() == "p":
        continue
    print(slovo, end="")

print()

for slovo in "Python Programer":
    if slovo.lower() == "g":
        break
    print(slovo, end="")

print()

for slovo in "Python Programer":
    if slovo.lower() == "o":
        pass  # Tu sam zaboravio implementirati nesto jako komplicirano ali budem jednog dana
    print(slovo, end="")

print()

broj = int(input("Upisite pozitivan broj : "))
while True:
    broj = broj - 1
    if broj % 2 == 0:
        continue
    print("Broj ", broj)
    if broj <= 0:
        break
    pass
pass
pass
print("Izasli smo iz petlje pomocu break-a")
