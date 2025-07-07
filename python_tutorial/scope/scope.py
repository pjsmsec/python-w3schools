# Scope
# A variable is only available from inside the region it is created.

# Local scope
def myfunc():
    x = 300
    print(x)

myfunc()

print()

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

print()

# Global scope
x = 300

def myfunc():
    print(x)

myfunc()

print(x)

# Naming varibles
# If you operate with the same varible name inside and outside of a function, 
# Python will treat them as two seperate variables, one only available in the 
# global scope (outside the function) and one available in the local scope (inside 
# the function)
x = 300

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)

print()

# global keyword
# If you need to create a global variable, but are stuck in the local scope, you 
# can use the global keyword.
def myfunc():
    global x
    x = 300

myfunc()

print(x)

print()

# Also, use the global keyword if you want to make a change to a global variable 
# inside a function.
x = 300

def myfunc():
    global x
    x = 200

myfunc()

print(x)

print()

# nonlocal keyword
# The nonlocal keyword is used with variables inside nested functions.
# The nonlocal keyword makes the variable velong to the outer function.
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) 
