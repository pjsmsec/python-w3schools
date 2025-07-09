# Bubble sort

# Steps:
# 1 - Go through the array, one value at a time.
# 2 - For each value, compare the value with the next value.
# 3 - If the value is higher than the next one, swap the values so that the highest 
#       value comes last.
# 4 - Go through the array as many times as there are values in the array.

mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(n - 1):
    for j in range(n - i - 1):
        if mylist[j] > mylist[j + 1]:
            mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]

print(mylist)

print()

# Bubble sort improvement
# In some cases the array will be sorted after the first run, but the algorithm will
# continue to run, without swapping elements, and thats not necessary.
# If the algorithm goes through the array one time withou swapping values, the 
# array must be sorted, and we can stop the algorithm

mylist = [7, 3, 9, 12, 11]

n = len(mylist)
for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if mylist[j] > mylist[j + 1]:
            mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
            swapped = True
    if not swapped:
        break

print(mylist)
