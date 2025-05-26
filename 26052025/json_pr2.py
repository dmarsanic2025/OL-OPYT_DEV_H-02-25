import json
from datetime import datetime

data = {"name": "John Doe", "crated_at": datetime.now()}


def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Objekt nije moguce serilizirat")


json_string = json.dumps(data, default=custom_serializer)

print(json_string)
