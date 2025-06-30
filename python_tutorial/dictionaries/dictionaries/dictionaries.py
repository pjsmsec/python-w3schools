thisdic = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1064
}

# Disctionaries are used to store data values in key:value pairs.
# It's a collection with is: ordered, changeable and does not allow ducplicates
print(thisdic)

print()

print(thisdic["brand"])

# Duplicates are NOT allowed

print()

print(len(thisdic))

print()

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print()

# type()
print(type(thisdic))

print()

# The dict() constructor
thisdic = dict(name = "John", age = 36, country = "Norway")

print(thisdic)
