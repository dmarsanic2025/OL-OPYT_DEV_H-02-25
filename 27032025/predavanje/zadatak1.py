vozni_park = {
    1: ["Kamion", "Iveco", "OS 001 ZZ", 2015, 45000.00],
    2: ["Kamion", "Iveco", "OS 002 ZZ", 2015, 47000.00],
    3: ["Tegljač", "MAN", "RI 001 ZZ", 2018, 78000.00],
    4: ["Tegljač", "MAN", "RI 002 ZZ", 2020, 97000.00],
    5: ["Kombi", "Mercedes Benz", "ST 001 ZZ", 2013, 12000.00],
    6: ["Kombi", "Volkswagen", "ST 002 ZZ", 2021, 35000.00],
    7: ["Dostavno vozilo", "Volkswagen", "ZG 001 ZZ", 2010, 9000.00],
    8: ["Dostavno vozilo", "Volkswagen", "ZG 002 ZZ", 2010, 9300.00],
}

print(f'\n{"_" *90}')
print(
    f"{'ID':<4}{'TIP':<18}{'Proizvodac':<15}{'Registarska oznaka':<20}{'Godina':<12}{'Cijena (EUR)':<10}"
)
print(f'\n{"_" *90}')

for kljuc, vrijednost in vozni_park.items():
    tip, proizvodac, reg_oznaka, godina, cijena = vrijednost
    print(
        f"{kljuc:<4}{tip:<18}{proizvodac:<15}{reg_oznaka:<20}{godina:<12}{cijena:,.2f}"
    )


print(f'\n{"_" *90}')
