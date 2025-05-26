import urllib
import urllib.parse
import urllib.request

upit = "programiranje u pythonu"

enkodiran_upit = urllib.parse.quote_plus(upit)

print(enkodiran_upit)

enkodiran_upit_utf8 = enkodiran_upit.encode("utf-8")

URL = f"https://www.google.com/search?q={enkodiran_upit_utf8.decode()}"

print(URL)

request = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})

with urllib.request.urlopen(request) as response:
    response_data = response.read().decode("utf-8")

print(response_data)
