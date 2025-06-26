print(10 > 9)
print(10 == 9)
print(10 < 9)

print()

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is notn greater than a")

print()

print(bool("Hello"))
print(bool(15))

print()

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print()

# Any number is True, except 0
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print(bool(0))
print(bool(None))
# None is also False

print()

# Other empy values are also False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print()

# One more value, or object in this case, evaluates to False, and that is if you 
# have an object that is made from a class with a __len__ function that returns 0 
# or False
class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()

print(bool(myobj))

print()

# Functions can return a Boolean
def myFunc():
    return True

print(myFunc())

print()

def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

print()

# Python also has many built-in functions that return a boolean value, like the 
# isinstance() function, which can be used to determine if an object is of a 
# certain data type
x = 200
print(isinstance(x, int))
