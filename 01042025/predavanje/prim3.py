import json

data = {"ime": "Ivan", "dob": 30, "zanimanja": ["programer", "kuhar"], "aktivan": True}
print(data)

print("*" * 70)

# Serilizacija u JSON
json_data = json.dumps(data)
print(json_data)

with open(r"01042025\predavanje\data.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

print("*" * 70)
with open(r"01042025\predavanje\data.json", "r", encoding="utf-8") as file:
    data_loaded = json.load(file)
    print(data_loaded)

# Deserilizacija iz JSON stringa
print("*" * 70)
data_from_json_data = json.loads(json_data)
print(data_from_json_data)
