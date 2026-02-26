"""
json.py
json → work with JSON data
dumps() → Python to JSON string
loads() → JSON string to Python
"""

import json

# Python dictionary
data = {
    "name": "Salamat",
    "age": 18,
    "city": "Almaty"
}

# Convert Python → JSON string
json_string = json.dumps(data)
print("JSON:", json_string)

# Convert JSON string → Python
parsed = json.loads(json_string)
print("Parsed name:", parsed["name"])
