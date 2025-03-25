prazan_tuple = ()

tuple_sa_jednim_elementom = (1,)

brojevi = (1, 2, 3, 4, 5)
razliciti_tipovi = (1, "Python", [1, 2, 3], {"kljuc": "vrijednost"})

print(razliciti_tipovi[0])
print(razliciti_tipovi[2][2])
print(razliciti_tipovi[-1])
# print(razliciti_tipovi[10])

tuple_pakiran = 1, 2, 3
print(type(tuple_pakiran))
print(tuple_pakiran)
a, b, c = tuple_pakiran
print(a, b, c)

razliciti_tipovi[2][0] = 2
print(razliciti_tipovi)

razliciti_tipovi[3]["kljuc"] = 2
print(razliciti_tipovi)
