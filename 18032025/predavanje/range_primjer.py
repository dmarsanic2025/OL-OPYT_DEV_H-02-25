"""
range(stop) -> generiraj raspon brojeva uvijek od 0 do vrijednosti definiranim argumentom stop - 1

range(start, stop) -> generiraj niz brojeva od broj definiranog argumentom start do broja definiranim argumentom stop - 1


range(start, stop, step) -> generiraj niz brojeva od broj
definiranog argumentom start do broja definiranim argumentom stop - 1, uz korak 'step'

"""

for i in range(5):
    print(i, end=" ")

print()

for i in range(1, 6):
    print(i, end=" ")

print()

for i in range(0, 10, 2):
    print(i, end=" ")

print()

for i in range(0, 5, 1):
    print(i, end=" ")

print()

# 10  8  6  4  2
for i in range(10, 0, -2):
    print(i, end=" ")
