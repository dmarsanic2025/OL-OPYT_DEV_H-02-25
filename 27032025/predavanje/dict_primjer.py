stanovnistvo = {
    "12345678901": "Petar Perić",
    "10987654321": "Marko Marić",
    "15975312345": "Ivan Ivić",
    "95135798765": "Josip Josipović",
}

element = stanovnistvo["10987654321"]
print(element)


# element = stanovnistvo["231231231"] pazi!!
element = stanovnistvo.get("231231231", "Ne postoji ovaj podatak!")
print(element)

element = stanovnistvo.get("10987654321")
print(element)


stanovnistvo["10987654321"] = "Patrik Mali"
print(stanovnistvo["10987654321"])

print("*" * 75)
for kljuc in stanovnistvo.keys():
    print(kljuc)
print("*" * 75)

for value in stanovnistvo.values():
    print(value)
print("*" * 75)

for kljuc, value in stanovnistvo.items():
    print(kljuc, value)
