# Lambda
# Syntax: lambda arguments: expression
x = lambda a : a + 10
print(x(5))

print()

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

print()

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

print()

def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

print()

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
