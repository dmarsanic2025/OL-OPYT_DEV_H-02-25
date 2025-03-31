brojevi = [1, 2, 3, 4, 5, 6]


def kvadrat(x):
    return x**2


kvadrati = list(map(kvadrat, brojevi))
kvadrati2 = list(map(lambda x: x**2, brojevi))

print(kvadrati)
print(kvadrati2)
