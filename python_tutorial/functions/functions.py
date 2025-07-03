def my_function():
    print("Hello from a function")

my_function()

print()

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

print()

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Renfnes")

print()

# Arbitrary arguments (*args)
# If you do not know how many arguments that will be passed into your function, add
# a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the item 
# accordingly:
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

print()

# Keyword arguments
# You can alse send arguments with the key = value syntax.

# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="Emil", child2="Tobias", child3="Linus")

print()

# Arbitrary keyword arguments (**kwargs)
# If you do not know how many keyword argumenrs that will be passed into your 
# function, add two asterisk ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the 
# items accordingly:
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

print()

# Default parameter value
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

print()

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

print()

def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

print()

def my_function():
    pass

print()

# Positional-only arguments
# You can specify that a function can ONLY have positional arguments, or ONLY 
# keyword arguments.

# To specify that a function can only have positional arguements, add , / after the 
# arguments.
def my_function(x, /):
    print(x)

my_function(3)

print()

# Without the , / you are actually allowed to use keyword arguments even if the 
# function expects positional arguments:
def my_function(x):
    print(x)

my_function(x = 3)

print()

# Keyword-only arguments

# To specify that a funtion can have only keyword arguments add *, before the 
# arguments: 
def my_function(*, x):
    print(x)

my_function(x = 3)

print()

# Combine positional-only and keyword-only

# Any argument before the / , are positional-only, and any argument after tue *, 
# are keyword-only
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

print()

# Recursion
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 3
    return result

print("Recursion Example Results:")
tri_recursion(6)
