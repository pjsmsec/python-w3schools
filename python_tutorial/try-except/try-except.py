# Try except
# The try black lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- 
# and except blocks.
try:
    print(x)
except:
    print("An exception occured")

print()

# Many exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

print()

# Else
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

print()

# Finally
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try excpt' is finished")

print()

# Example: try to open and write a file that is not writable:
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

print()

# Raise an exception

# x = -1

# if x < 0:
#     raise Exception("Sorry, no numbers below zero")
# The raise keyword raises exceptions

print()

x = "hello"

if not type(x) is int:
    raise TypeError("only integers are allowed")
