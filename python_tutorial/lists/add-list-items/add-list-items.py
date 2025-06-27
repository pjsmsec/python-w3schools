thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist.append("orange")
print(thislist)

print()

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist.insert(1, "orange")
print(thislist)

print()

# Extend list
# Apppends elements from another list to the current one
thislist = ["apple", "banana", "cherry"]
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(tropical)
print(thislist)

print()

# Add any iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi","orange")
print(thislist)

thislist.extend(thislist)
print(thistuple)
print(thislist)
