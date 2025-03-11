"""
Ako automobil troši 5.3 litara na 100 km i ako je cijena goriva 9.56 kn
po litri (nije važno kojeg goriva), izračunajte koliko košta 1 km vožnje
automobilom. Prikažite mjesečni trošak (30 dana) odlaska na posao
automobilom koji je udaljen 20 km u jednom smjeru.
"""

potrosnja_na_100km = 5.3
cijena_po_litri = 9.56
udaljenost_u_oba_smjera = 20 * 2
BROJ_DANA_U_MJESECU = 30

trosak_po_km = (potrosnja_na_100km / 100) * cijena_po_litri

mjesecni_trosak = trosak_po_km * udaljenost_u_oba_smjera * BROJ_DANA_U_MJESECU


print(mjesecni_trosak, "kn")
