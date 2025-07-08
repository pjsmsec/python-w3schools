# Write to an existing file
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
with open("demofile.txt", "a") as f:
    f.write("Now the file has more content!")

with open("demofile.txt") as f:
    print(f.read())

print()

# Overwrite existing content
with open("demofile.txt", "w") as f:
    f.write("Whoops! I have deleted the content!")

with open("demofile.txt") as f:
    print(f.read())

# Create a new (empty) file
f = open("myfile.txt", "x")