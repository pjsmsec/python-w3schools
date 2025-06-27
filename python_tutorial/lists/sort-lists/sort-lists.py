# Sort lists alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()

print(thislist)

print()

thislist = [100, 50, 65, 82, 23]
thislist.sort()

print(thislist)

print()

# Sort descencing
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)

print(thislist)

print()

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)

print(thislist)

print()

# Customize sort function
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

print()

# Case insensitive sort
# By default the sort() method is case sensitive, resulting ins all capital 
# letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

print()

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

print()

# Reverse order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
