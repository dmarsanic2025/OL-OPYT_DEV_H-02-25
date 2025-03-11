poruka = "Hello, world!"

prvi_znak = poruka[0]
posljednji_znak = poruka[-1]

print(poruka)
print(prvi_znak)
print(posljednji_znak)
print(poruka[12])
print(poruka[len(poruka) - 1])

print("***********")
print(len(poruka))

for znak in poruka:
    print(znak, end=" ")
