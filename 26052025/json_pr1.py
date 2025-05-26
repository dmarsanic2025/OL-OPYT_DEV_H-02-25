import json


data = {"name": "John Doe", "age": 30, "is_student": False}

json_string = json.dumps(data)

print(json_string)


json_string2 = '{"name": "John Doe", "age": 30, "is_student": false}'

data2 = json.loads(json_string2)

print(data2)


with open("data.json", "w") as file:
    json.dump(data, file, indent=4)


with open("data.json", "r") as file:
    data3 = json.load(file)

print(data3)
