import requests

URL = "http://example.com/api"

data = {"name": "John Doe", "email": "jdoe@gdasca.com"}

response = requests.post(URL, data=data)

if response.status_code == 200:
    print("Sadrzaj : \n", response.text)
else:
    print(response.status_code)
