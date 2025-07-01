thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in thisdict:
    print(f"{x} - {thisdict[x]}")

print()

# You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
    print(x)

print()

# You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
    print(x)

print()

# You can loop through the keys AND values by using the items() method:
for x, y in thisdict.items():
    print(x, y)
