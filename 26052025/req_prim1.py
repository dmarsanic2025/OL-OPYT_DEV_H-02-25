import requests

URL = "https://www.algebra.hr/"

response = requests.get(URL)

if response.status_code == 200:
    print("Sadrzaj : \n", response.text)
else:
    print(response.status_code)
