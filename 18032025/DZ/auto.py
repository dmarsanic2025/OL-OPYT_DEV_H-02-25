"""
Ako automobil troši 5.3 litara na 100 km i ako je cijena goriva 9.56 kn
po litri (nije važno kojeg goriva), izračunajte koliko košta 1 km vožnje
automobilom. Prikažite mjesečni trošak (30 dana) odlaska na posao
automobilom koji je udaljen 20 km u jednom smjeru.

SA INPUT FUNKCIJOM
"""

potrosnja_na_100km = float(input("Upišite koliko auto troši na 100km: "))
cijena_po_litri = float(input("Upišite koliko košta 1l goriva: "))
udaljenost_u_oba_smjera = int(input("Upišite udaljenosti do vašeg posla: ")) * 2
BROJ_DANA_U_MJESECU = 30

trosak_po_km = (potrosnja_na_100km / 100) * cijena_po_litri

mjesecni_trosak = trosak_po_km * udaljenost_u_oba_smjera * BROJ_DANA_U_MJESECU


print(mjesecni_trosak, "kn")
