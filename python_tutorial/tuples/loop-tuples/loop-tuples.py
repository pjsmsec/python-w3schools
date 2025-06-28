thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

print()

# Loop through the index numbers
# Use the range() and len() functions to create a suitable iterable
for i in range(len(thistuple)):
    print(thistuple[i])

print()

# Using a while loop
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1
