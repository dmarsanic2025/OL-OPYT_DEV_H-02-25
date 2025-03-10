"""
 • Imate 10000 kn i možete zaboraviti na njih na 15 godina. Ako Vam
banka nudi 2.5% godišnju kamatu za taj iznos, koliko ćete zaraditi
nakon 15 godina. Jednostavni kamatni račun k = C * p * t
 • k = iznos kamata odnosno prinos
 • C = iznos glavnice
 • p = godišnja kamatna stopa – NAPOMENA: 5% = 5 / 100 = 0.05
 • t = vrijeme u godinama
"""

C = 10_000  # kn
p = 2.5 / 100
t = 15  # g

k = C * p * t
ukupno = k + C  # Ukupan iznos nakon sto prode 15g

print(k, "kn")
print(ukupno, "kn")
