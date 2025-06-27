# One cannot copy a list by typing list2 = list1 because list2 will only be a 
# reference to list1, and changes made to list1 will automatically be made in 
# list2

# copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()

print(mylist)

print()

# Use the list() method
mylist = list(thislist)
print(mylist)
