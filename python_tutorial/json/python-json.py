import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["age"]) 

print()

# COnvert from python to json
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)

print(y)

print()

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print()

# Example: convert a python object containing all the legal types:
import json

x = {
    "name": "John",
    "age": 20,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

print()

# Formatting json.dumps() result
# Use the indent parameter to define the numbers of indents
json.dumps(x, indent=4)
print(x)

print()

# Use the seperators parameter to change the default separator:
json.dumps(x, indent=4, separators=(". ", " = "))
print(x)

print()

# Order the result
# The json.dumps() method has parameters ot order the keys in the result:
# Use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True)
print(x)
