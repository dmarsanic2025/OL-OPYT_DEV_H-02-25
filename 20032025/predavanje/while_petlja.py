# while int(input("Upisite broj veci od 5 :")) > 5:
#    print(f"Upisali ste broj koji je veci od 5")

# print("Petlja WHILE je zavrsila")


broj = int(input("Upisite pozitivan broj : "))

while broj > 0:
    print("Broj ", broj)
    broj = broj - 1
else:  # ne trebate koristiti else sa while ili for
    print("petlja je zavrsena jer je broj manji ili jednak nuli")

print("Neki drugi bezveze tekst")
