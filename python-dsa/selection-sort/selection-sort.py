# Selection sort

# Steps
# 1 - Go through the array to find the lowest value.
# 2 - Move the lowest value to the front of the unsorted part of the array.
# 3 - Go through the array again as many times as there are values in the array.

mylist = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(mylist)
for i in range(n -1):
    min_index = i
    for j in range(i + 1, n):
        if mylist[j] < mylist[min_index]:
            min_index = j
    min_value = mylist.pop(min_index)
    mylist.insert(i, min_value)

print(mylist)

print()

# Improved selection sort

# Each time a value is removed to be moved to the head of the array, all following
# array elements must be shifted one place down in the array.
# Swaping values instead of removing, moving and shifting solves that issue.

mylist = [64, 34, 25, 12, 22, 11, 90, 5]
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(n):
  min_index = i
  for j in range(i+1, n):
     if mylist[j] < mylist[min_index]:
       min_index = j
  mylist[i], mylist[min_index] = mylist[min_index], mylist[i]

print(mylist)
