# Change tuple values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

print()

# Add items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

print()

thistuple = ("apple", "banana", "kiwi")
y = ("orange",)
thistuple += y

print(thistuple)

print()

# Remove items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

print()

# The del() keyword can delete a tuple completely
thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)
# This will raise an error because the tuple no longer exists
