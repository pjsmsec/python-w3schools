f = open("demofile.txt")

print(f.read())
# File path might be necessary

print()

# Using the with statement
# The with statement closes the file automatically
with open("demofile.txt") as f:
    print(f.read())

print()

# Close files
f = open("demofile.txt")
print(f.readline())
f.close()

print()

# Read only parts of the file
# By default the read() method returns the whole text but the number of charactes
# can be defined
with open("demofile.txt") as f:
    print(f.read(5))

print()

# Read lines
with open("demofile.txt") as f:
    print(f.readline())

# It can be used in sequence
with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())

print()

# Looping through the file lines
with open("demofile.txt") as f:
    for x in f:
        print(x)
