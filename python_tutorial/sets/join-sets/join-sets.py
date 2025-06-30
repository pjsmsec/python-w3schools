# union() and update() methods join two or more sets
# intersection() keeps only the duplicates
# difference() keeps the items from the first set that are not in the other sets
# symmetric_difference() keeps all items EXCEPT the duplicates

# union()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)

print(set3)

print()

# You can use the | operator instead of the union() method
set3 = set1 | set2

print(set3)

print()

set3 = {"John", "Elena"}
set4 = {"apple", "banana", "cherry"}

myset = set1.union(set2, set3, set4)

print(myset)

print()

# Using the | operator, seperate the sets with more | operators:
myset = set1 | set1 | set3 | set4

print(myset)

print()

# Join a set and a tuple
# The union() method allows to join a set with other data types
x = {"a", "b", "c"}
y = {1, 2, 3}

z = x.union(y)

print(z)
# Note: the | operator only allows you to join sets with sets

print()

# update()
# The update() method inserts all items from one set into another.
# It changes the original set, and does not return a new set
set1 = x
set2 = y

set1.update(set2)

print(set1)
# Note: both union() and update() will exclude any duplicate items.

print()

# intersection()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)

print(set3)

print()

# You can use the & operator instead of the intersection() method:
set3 = set1 & set2

print(set3)
# Note: the & operator only allows you to join sets with sets

print()

# intersection_update() method will only keep the duplicates, but will change the
# original set
set1.intersection_update(set2)

print(set1)

print()

set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", True}

set3 = set1.intersection(set2)

print(set3)

print()

# difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

print()

# Use the - operator instead oif the difference() method
set3 = set1 - set2

print(set3)
# Note: the - operator only allows you to join sets with sets

print()

# The difference_update()
# Will also keep the items from the first set that are not in the other set, but it
# will change the original set
set1.difference_update(set2)

print(set1)

print()

# simmetic_difference()
# Will keep only the elements that are NOT present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

print()

# You can use the ^ operator instead of the symmetric_difference() method
set3 = set1 ^ set2

print(set3)
# Note: the ^ operator allows you to join sets with sets

print()

# symmetric_difference_update()
# Will also keep all but the duplicates, but it will change the original set 
# insteand of returning set
set1.symmetric_difference_update(set2)

print(set1)
