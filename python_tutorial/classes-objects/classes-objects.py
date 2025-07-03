# Create class
class MyClass:
    x = 5

# Create object
# Example: create an object named p1, and print the value of x
p1 = MyClass()
print(p1.x)

print()

# The __init__() function
# All classes have a build-in function called __init__(), which is always 
# executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other 
# operations that are necessary to to when the object is being created:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
# Note: the __init__() function is called automatically every time the class is 
# being used to create a new object.

print()

# The __str__() function
# The __ste__() function controls what should be returned when the class object is 
# represented as a string

# If the __str__() function is not set, the string representation of the object is 
# returned:

# Example: the string representation of an object WITHOUT the __str__() function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1)

print()

# Example: the string representation of an object WITH the __str__() function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("John", 36)

print(p1)

print()

# Object methods
# Objects can also contain methods.
# Methods in objects are functions that belong to the object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
# Note: the self parameter is a reference to the current instance of the class, and 
# is used to access variables that belong to the class.

print()

# The self parameter
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    
    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

print()

# Modify object properties
# You can modify properties on objects:

# Example: set the age of p1 to 40:
p1.age = 40

print()

# Delete object properties
# You can delete properties on objects by using the del keyword:

# Example: delete the age property from the p1 object:
del p1.age

# Delete objects
# You can delete objects by using the del keyword:
del p1

# The pass statement
# class definitions cannot be empty, use the pass statement to avoid raising errors.
class Person:
    pass
