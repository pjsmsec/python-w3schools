thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

print()

# Negative indexing
print(thistuple[-1])

print()

# Range of indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

print()

print(thistuple[:4])

print()

print(thistuple[2:])

print()

# Range of negative indexes
print(thistuple[-4:-1])

print()

# Check if item exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
