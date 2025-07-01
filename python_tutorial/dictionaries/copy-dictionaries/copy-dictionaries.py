thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

mydict = thisdict.copy()

print(mydict)

print()

# Another way to copy a dictionary is to use the dict() function:
mydict = dict(thisdict)

print(mydict)
