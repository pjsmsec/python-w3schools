myset = {"apple", "banana", "cherry"}
print(myset)

# Duplicates not allowed
# Note: the values True and 1 are considereded the same value in sets, and are 
# treated as duplicates

print()

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

print()

# Note: the values False and 0 are considered the same in sets, and are treated
# as duplicates
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

print()

# Get the length of a set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

print()

# Set items can be of any data type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set4 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))

print()

# The set() constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)
