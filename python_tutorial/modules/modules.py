# import mymodule

# mymodule.greeting("Jonathan")

print()

# a = mymodule.person1["age"]
# print(a)

# Re-naming a module
import mymodule as mx

a = mx.person1["age"]
print(a)

print()

import platform

x = platform.system()
print(x)

print()

# Using the dir() function
# Lists all the function and variable names in a module
x = dir(platform)
print(x)

print()

# import from module
# Partial importing
from mymodule import person1

print(person1["age"])
