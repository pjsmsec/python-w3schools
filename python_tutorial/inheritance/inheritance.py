class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

print()

# Create a child class
class Student(Person):
    pass
# Note: the pass keyword is used because nothing was added to the Student child 
# class

x = Student("Mike", "Olsen")
x.printname()

print()

class Student(Person):
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
x = Student("Mike", "Olsen")
x.printname()

# When you add the __init__() function, the child class will no longer inherit 
# the parent's __init__() function

# The child's __init__() function overrides the inheritance of the parent's 
# __init__() function

print()

# To keep the inheritance of the parent's __init__() function, add a call to the
# parent's __init__() function:
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()

print()

# The super() function will make the child class inherit all the methods and 
# properties from it's parent:
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
    
x = Student("Mike", "Olsen")
x.printname()

print()

# Add properties
# Example: add a property called graduationyear to the Student class:
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname. lname)
        self.graduationyear = 2019

# graduationyear should have been a variable passed into the Student class
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
x.printname()

print()

# Add methods
# Example: add a method called welcome to the Student class:
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x .welcome()

# If you add a method in the child class with the same name as a function in the 
# parent class, the inheritance of the parent method will be overridden.
 