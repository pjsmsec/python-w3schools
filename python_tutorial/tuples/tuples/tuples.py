# A tuple is a collection which is ordered and unchangeable

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple items can be accessed by index (like list items)

print()

# Allow duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print()

# Tuple length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

print()

# Create tuple with one item
thistuple = ("apple",)
print(type(thistuple))

print()

# NOT a tuple -> string
thistuple = ("apple")
print(type(thistuple))

print()

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# Tuples can contain different data types
tuple1 = ("abc", 34, True, 40, "male")

print()

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

print()

# The tuple() constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
