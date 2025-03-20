# Ispišite zbroj brojeva od 1 do 10.

zbroj = 0
for i in range(1, 10):  # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
    # zbroj = zbroj + i
    zbroj += i

print(f"Zbroj brojeva od 1 do 10 je : {zbroj}")

# Ispišite umnozak brojeva od 1 do 10.

umnozak = 1
for i in range(1, 10):  # 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9
    umnozak = umnozak * i
    # umnozak *= i

print(f"Umnozak brojeva od 1 do 10 je : {umnozak}")
