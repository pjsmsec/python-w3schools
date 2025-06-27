fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

print()

newlist = [x for x in fruits if "a" in x]

print(newlist)

print()

newlist = [x for x in fruits if x != "apple"]

print(newlist)

print()

# Note: the condition is optional and can be omitted
newlist = [x for x in fruits]

print(newlist)

print()

# It can be performed on any iterable
newlist = [x for x in range(10)]

print(newlist)

print()

newlist = [x for x in range(10) if x < 5]

print(newlist)

print()

newlist = [x.upper() for x in fruits]

print(newlist)

print()

# Note: you can set the outcome to whatever you like:
newlist = ['hello' for x in fruits]

print(newlist)

print()

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
