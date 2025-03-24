"""
Ispišite sve troznamenkaste brojeve čiji je zbroj znamenaka veći od 10 koristeći se petljom while (Koristiti se
% modulo operacijom.).
"""

# prvi troznamenkasti broj 100
# zadnji ... broj je 999
# 759 // 10 = 75 % 10 = 5
broj = 100
while broj < 999:
    stotica = broj // 100
    desetica = (broj // 10) % 10
    jedinice = broj % 10

    if jedinice + desetica + stotica > 10:
        print(broj)

    broj += 1
