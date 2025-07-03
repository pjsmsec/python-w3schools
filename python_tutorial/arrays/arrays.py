cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print()

print(x)

cars[0] = "Toyota"

print(cars)
print(cars[0])

print()

x = len(cars)

print(x)

print()

for x in cars:
    print(x)

print()

# Adding array elements
cars.append("Honda")

print(cars)

print()

# Removing array elements

# Example: delete the second element of the cars array
print(cars)
cars.pop(1)
print(cars)

print()

cars.remove("BMW")
print(cars)
