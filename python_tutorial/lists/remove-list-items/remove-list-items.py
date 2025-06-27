thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist.remove("banana")
print(thislist)

print()

# Removes the first occurence
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)

thislist.remove("banana")
print(thislist)

print()

# Remove specified index
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist.pop(1)
print(thislist)

print()

# Unless specified, pop() removes the last item
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist.pop()
print(thislist)

print()

# The del keyword removes the specified index
thislist = ["apple", "banana", "cherry"]
print(thislist)

del thislist[0]
print(thislist)

print()

# clear() the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
