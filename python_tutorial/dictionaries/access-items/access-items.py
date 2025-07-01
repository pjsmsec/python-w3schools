thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisdict["model"]

print(x)

print()

# You can also use the get() method to get the same result
x = thisdict.get("model")

print(x)

print()

# Get keys
# The keys() method will return a list of all the keys in a dictionary.
x = thisdict.keys()

print (x)

print()

# Example:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)

car["color"] = "white"

print(x)

print()

# The values() method will return a list of all the values in the dictionary
x = thisdict.values()

print(x)

print()

# Example:
x = car.values()

print(x)

car["year"] = 2020

print(x)

car["color"] = "red"

print(x)

print()

# Check if key exists
# To dertermine if a specified key is present in a dictionary use the in keyword:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in this dictionary")
