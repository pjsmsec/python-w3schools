thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

print()

# Loop through the index numbers
# You can loop through the list items by referring to their index number,
# USe the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

print()

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

print()

# Looping useing list comprehension
[print(x) for x in thislist]
