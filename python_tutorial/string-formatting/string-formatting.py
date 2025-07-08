# F-strings
txt = f"The price is 49 dollars."

print(txt)

print()

# Placeholders and modifiers
price = 59
txt = f"The price is {price} dollars."

print(txt)

print()

txt = f"The price is {price:.2f} dollars."

print(txt)

print()

txt = f"The price is {95:.2f} dollars."

print(txt)

print()

# Operations in f-strings
txt = f"The price is {20 * 59} dollars."

print(txt)

print()

price = 59
tax = 0.25
txt = f"The price is {price * tax} dollars."

print(txt)

print()

# if...else
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}."

print(txt)

print()

# Execute functions in f-strings
fruit = "apples"
txt = f"I love {fruit.upper()}!"

print(txt)

print()

def myconverter(x):
    return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude."

print(txt)

print()

# Example: use a comma as a thousand separator:
price = 59000 
txt = f"The price is {price:,} dollars."

print(txt)

print()

# String format()
price = 49
txt = "The price is {} dollars."

print(txt.format(price))

print()

txt = "The price is {:.2f} dollars."

print(txt.format(price))

print()

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."

print(myorder.format(quantity, itemno, price))

print()

# Index numbers
# You can use index numbers (a number inside the curly brackets {0}) to be sure the 
# values are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."

print(myorder.format(quantity, itemno, price))

print()

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."

print(txt.format(age, name))

print()

# Named indexes
myorder = "I have a {carname}, it is a {model}."

print(myorder.format(carname="Ford", model= "Mustang"))
