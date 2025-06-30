thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
# Note: if the item to remove does not exist, remove() will raise an error

print(thisset)

print()

thisset.discard("banana")

print(thisset)
# Note: if the item to remove does not exit, discard() will not raise an error

print()

# pop()
# This method will remove a random item
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)
print(thisset)

print()

# clear()
# This method returns ()
thisset.clear()

print(thisset)

print()

# del()
# This keyword deletes the set completly and may raise arrors
del thisset

print(thisset)
