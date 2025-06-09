# 📝 ZADATAK: To-Do Lista (HTML, CSS, JavaScript)

## 🎯 Cilj
Napraviti jednostavnu **To-Do web aplikaciju** koja omogućuje korisniku da:
- dodaje zadatke,
- označava ih kao dovršene,
- briše ih iz liste,
- i (opcionalno) sprema ih u `localStorage` za trajno pohranjivanje.

---

## 🗂️ Struktura projekta
```
to-do-app/
├── index.html
├── style.css
└── script.js
```

## 📌 Zahtjevi

### 1. HTML (`index.html`)
- Napravi stranicu s naslovom **"To-Do Lista"**
- U tijelu stranice mora se nalaziti:
  - jedan **input** za unos novog zadatka
  - gumb **"Dodaj zadatak"**
  - prazna **ul lista** za prikaz zadataka
  - paragraf za prikaz broja nedovršenih zadataka (kasnije)

---

### 2. CSS (`style.css`)
- Centriraj aplikaciju na sredinu ekrana
- Stiliziraj:
  - input i gumb tako da budu pregledni i funkcionalni
  - listu zadataka tako da:
    - svaki zadatak bude u vlastitom okruženju (`li`)
    - dovršeni zadaci budu precrtani i sivi
    - svaki zadatak ima gumb **"Ukloni"**
  - dodaj **hover efekte** za gumbe

---

### 3. JavaScript (`script.js`)
Implementiraj sljedeće funkcionalnosti:

#### Osnovno:
- Klikom na "Dodaj zadatak":
  - pročitaj vrijednost iz inputa
  - napravi novi `<li>` element s tekstom zadatka
  - dodaj ga u listu
- Klikom na zadatak:
  - označi/odznači ga kao dovršen (`.completed`)
- Klikom na gumb "Ukloni":
  - ukloni zadatak iz liste
- Ako korisnik klikne "Dodaj zadatak", a input je prazan:
  - prikaži upozorenje (alert)

#### Bonus (ako imaš dodatnog vremena):
- Prikazuj broj preostalih **nedovršenih** zadataka
- Spremi zadatke u **localStorage**
- Kad se stranica ponovno učita, prikazuj zadatke iz `localStorage`

---

## ✅ Primjeri ponašanja

### ➕ Dodavanje zadatka:
Unosom teksta i klikom na "Dodaj zadatak", novi zadatak se prikazuje u listi s gumbom "Ukloni".

### ✔️ Označavanje zadatka:
Klikom na tekst zadatka, on se označava kao dovršen (precrtan) i broj nedovršenih se ažurira.

### ❌ Uklanjanje zadatka:
Klikom na gumb "Ukloni", taj zadatak nestaje s liste.

### 💾 Pohrana:
Ako se implementira `localStorage`, zadaci ostaju vidljivi i nakon što se stranica ponovno učita.

---

## 🕒 Procijenjeno vrijeme: 2 sata

---