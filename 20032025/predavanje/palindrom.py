rijec = "ammmmmmfa"
duzina = len(rijec)
palindrom = True
# kajak -> duzina 5 -> 5//2 -> 2
# 01234
for i in range(duzina // 2):
    if rijec[i] != rijec[-(i + 1)]:
        palindrom = False
        # break ovo nismo jos ucili ali optimiziraniji nacin
# rijec = "ammmmmmfa"

if palindrom:
    print(f'Riječ "{rijec}" je palindrom.')
else:
    print(f'Riječ "{rijec}" nije palindrom.')
