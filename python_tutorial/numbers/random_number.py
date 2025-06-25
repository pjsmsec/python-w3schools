# Python does not have a random() function.
# It requires the random built-in module
import random

print(random.randrange(1, 10))

print()

acc = 0

while acc < 10:
    print(random.randrange(1, 100))
    acc += 1
