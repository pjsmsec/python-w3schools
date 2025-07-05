# Iterators
# An object which implements the iterator protocol, which consists of the methods
# __inter__() and __next__()

# Example: return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print()

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print()

# Looping through an iterator
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

print()

mystr = "banana"

for x in mystr:
    print(x)
# The for loop actually creates an iterator object and executes the next() method
# for each loop

print()

# Create an iterator
# The methods __iter__() and __next__() need to be implemented.
class MyNymbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNymbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print()

# Stop iteration
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
