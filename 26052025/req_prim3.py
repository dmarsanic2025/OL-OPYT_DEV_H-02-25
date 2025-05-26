import requests
from requests.auth import HTTPBasicAuth

URL = "http://example.com/login"


response = requests.get(URL, auth=HTTPBasicAuth("username", "password"))

if response.status_code == 200:
    print("Sadrzaj : \n", response.text)
else:
    print(response.status_code)
