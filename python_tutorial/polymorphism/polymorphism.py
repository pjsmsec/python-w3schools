# Polymorphism
# Methods/Functions/Operators with the same name that can be executed on many 
# objects or classes

# Example: the len() function
x = "Hello World!"
mytuple = ("apple", "banana", "cherry")
thisdic = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(len(x))
print(len(mytuple))
print(len(thisdic))

print()

# Example: different classes with the same method:
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()

print()

# Inheritance class polymorphism
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")
    
class Plane(Vehicle):
    def move(self):
        print("Fly!")

car2 = Car("Ford", "Mustang")
boat2 = Boat("Ibiza", "Touring 20")
plane2 = Plane("Boeing", "747")

for x in (car2, boat2, plane2):
    print(x.brand)
    print(x.model)
    x.move()
