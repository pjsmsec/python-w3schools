# 'hello' is the same as "hello"
print("hello")
print('hello')

print()

# Quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

print()

a = "Hello"

print(a)

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""

print(b)

print()

# Strings are arrays
a = "Hello, World!"

print(a[1])

print()

# Looping through a string
for x in "banana":
    print(x)

print()

# String length
a = "Hello, World"

print(len(a))

print()

# Check string
txt = "The best things in life are free"

print("free" in txt)

print()

if "free" in txt:
    print("Yes, 'free' is present.")

print()

# Check if not
print("expensive" not in txt)

print()

if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
