"""
 Kreirajte varijable (imenujte ih i dodijelite im odgovarajuću 
vrijednost) te ispišite na ekran odgovarajuće vrijednosti, za:
 • Ime, prezime, godinu rođenja, državu rođenja, status radnog odnosa, 
težinu te spol
 • Stranice a i b, četverokuta te za površinu tog četverokuta.
 • Izračun mjesečne potrošnje el. struje te cijene el. struje koju potroši 
mikrovalna pećnica snage 1,3 kW ako se koristi 2 sata dnevno?
 • Stranice trokuta, površinu trokuta (P = a*va) / 2 te opseg trokuta
"""

# 1.
ime = 'Ivan'
prezime = 'Horvat'
god_rodenja = 1995
drzava_rodenja = 'Hrvatska'
status_radnog_odnosa = 'Zaposlen'
tezina = 55 #kg
spol = 'M'

print(ime)
print(prezime)
print(god_rodenja)
print(drzava_rodenja)
print(status_radnog_odnosa)
print(tezina)
print(spol)
#
print('---------------------')
print(ime, prezime, god_rodenja, drzava_rodenja, status_radnog_odnosa, tezina, spol, sep='\n')

# 2 . 
# Stranice četverokuta i izračun površine
a = 5
b = 8
# povrsina_cetverokuta = a * b
print(a, '*', b, '=', a * b)

# 3.
snaga_mikrovalne = 1.3 #kW
vrijeme_koristenja = 2 #sati
cijena_struje = 1 #EUR/kWh

mjesecna_potrosnja_kwh = snaga_mikrovalne * vrijeme_koristenja * 30
mjesecna_cijena = mjesecna_potrosnja_kwh * cijena_struje

print('Mjesecni trosak ', mjesecna_cijena, '€')

# 4. Za DZ
