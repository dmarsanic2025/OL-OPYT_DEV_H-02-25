import requests
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/coronavirus/"

covid_stranica = BeautifulSoup(requests.get(URL).content, "html.parser")

svi_podaci = covid_stranica.find_all("div", id="maincounter-wrap")

# print(svi_podaci)

for item in svi_podaci:
    naslov = item.find("h1").get_text()
    vrijednost = item.find("span").get_text()
    print(naslov, vrijednost.replace(",", ""))
