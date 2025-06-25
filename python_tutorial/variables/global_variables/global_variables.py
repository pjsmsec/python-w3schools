# Global variables are created outside of functions
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

print()

# Variables created inside a function have their scope limited to said function
# If two variables have the same name, one global and one local, during the 
# function's execution, the local variable will be used
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

print()

# global keyword
# Using the global keyword inside a function will change tha variable's scope
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
