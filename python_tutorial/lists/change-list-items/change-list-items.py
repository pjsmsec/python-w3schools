thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist[1] = "blackcurrant"
print(thislist)

print()

# Change a range of item values
thislist =  ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# Note: the length of the list will change when the number of items inserted does
# not match the number of items replaced

print()

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist[1:3] = ["watermelon"]
print(thislist)

print()

# Insert items
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist.insert(2, "watermelon")
print(thislist)
