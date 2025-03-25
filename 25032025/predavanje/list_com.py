brojevi = [1, 2, 3, 4, 5]

brojevi_kvadrat = []
for broj in brojevi:
    brojevi_kvadrat.append(broj**2)

print(brojevi_kvadrat)

brojevi_kvadrat2 = [broj**2 for broj in brojevi]
print(brojevi_kvadrat2)

parnost = []
for broj in brojevi:
    if broj % 2 == 0:
        parnost.append("paran")
    else:
        parnost.append("neparan")


parnost = ["paran" if broj % 2 == 0 else "neparan" for broj in brojevi]
print(parnost)

kvadrati_parnih_brojeva = [broj**2 for broj in brojevi if broj % 2 == 0]
print(kvadrati_parnih_brojeva)
