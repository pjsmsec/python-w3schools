# The pop() method removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.pop("model")

print(thisdict)

print()

# The popitem() method removes the last inserted item
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.popitem()

print(thisdict)

print()

# The del keyword deletes a dictionary completely:
del thisdict
# pint(thisdict)
# This will raise an error since the dictionary no longer exists

# The clar() method empties a dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.clear()

print(thisdict)
