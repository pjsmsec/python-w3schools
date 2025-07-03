fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print()

for x in fruits:
    if x == "banana":
        break
    print(x)

print()

for x in fruits:
    if x == "banana":
        continue
    print(x)

print()

# The range() function
# Returns a sequence of numbers, starting from 0 by default, and increments by 1 
# (by default), and ends at a specified number.
for x in range(6):
    print(x)

print()

# Non-default ranges
for x in range(2, 6):
    print(x)

# Ranges with steps
for x in range(2, 30, 3):
    print(x)

print()

for x in range(6):
    print(x)
else:
    print("Finally finished!")

print()

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

print()

# Nested loops
adj = ["red", "bit", "tasty"]
fruits = ["apple" "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

print()

# The pass statement
# for loops cannot be empty, but if you for some reason have a for loop without 
# content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
    pass
