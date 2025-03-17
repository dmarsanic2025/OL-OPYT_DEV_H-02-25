# 8c03fc
boja = "8c03fc"

r = int(boja[0:2], 16)
g = int(boja[2:4], 16)
b = int(boja[4:6], 16)

print(r, g, b)


print(hex(r)[2:].zfill(2), hex(g)[2:].zfill(2), hex(b)[2:].zfill(2), sep="")
print(f"{hex(r)[2:]:02}{hex(g)[2:]:02}{hex(b)[2:]:02}")
