a = 33
b = 200

if b > a:
    print("b is greater than a")

# Note: in Python, indentation has meaning

print()

# The elif keyword
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

print()

a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

print()

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print()

# Short hand if
if a > b: print("a is greater than b")

print()

# Short hand if ... else
a = 2
b = 330

print("A") if a > b else print("B")

print()

# Example:
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")

print()

a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")

print()

if a > b or a > c:
    print("At least one of the conditions is True")

print()

a = 33
b = 200

if not a > b:
    print("a is NOT greater than b")

print()

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also abore 20!")
    else:
        print("but not abore 20.")

print()

# if statements cannot be empty, but if you for some reason have an if statement 
# with no comment, put in the pass statement to avoid getting an error
a = 33
b = 200

if b > a:
    pass
