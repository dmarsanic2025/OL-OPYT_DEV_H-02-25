try:
    rezultat = 10 / 0

except ZeroDivisionError as e:
    print(f"Sad smo tu {e}")
except Exception as e:
    print(f"Dogodila se neka greška: {e}")

print("*" * 70)
try:
    rezultat = 10 / float(input("Upisi neki broj"))
except ZeroDivisionError as e:
    print(f"Sad smo tu {e}")
except TypeError as e:
    print(f"E sada smo cak tu {e}")
except Exception as e:
    print(f"Dogodila se neka greška: {e}")

print("*" * 70)
try:
    rezultat = 10 / 1
except ZeroDivisionError as e:
    print(f"Sad smo tu {e}")
except Exception as e:
    print(f"Dogodila se neka greška: {e}")
else:
    print("Nije desilo nista lose")


print("*" * 70)
try:
    rezultat = 10 / 0
except ZeroDivisionError as e:
    print(f"Sad smo tu {e}")
except Exception as e:
    print(f"Dogodila se neka greška: {e}")
else:
    print("Nije desilo nista lose")
finally:
    print("ovaj blok se izvrsava uvijek!")

print(rezultat)
print("Program se nije zgasio mozemo programirati dalje")


unos_teksta = input("Unesi neki tekst: ")
try:
    if unos_teksta == "":
        raise ValueError("Nisi ništa unio")
except ValueError:
    print("Dogodila se greskica")

unos = input("Upisi neki broj")
if unos.isnumeric():
    unos = float(unos)
else:
    raise ValueError("Nisi upisao broj!")
