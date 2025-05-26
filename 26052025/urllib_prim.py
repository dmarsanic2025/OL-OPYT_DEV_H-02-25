import urllib
import urllib.request

URL = "https://www.algebra.hr/"

konekcija = urllib.request.urlopen(URL)

html_stranica = konekcija.read().decode()

print(html_stranica)
