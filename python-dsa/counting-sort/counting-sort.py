# Counting sort

# Steps:
# 1 - Create a new array for counting how many there are of the different values.
# 2 - Go through the array that needs to be sorted.
# 3 - For each value, count it by increasing the counting array at the corresponding 
#       index.
# 4 - After counting the values, go through the counting array to create the sorted 
#       array.
# 5 - For each count in the counting array, create the correct number of elements, 
#       with values that correspond to the counting array index.

def countingSort(arr):
  max_val = max(arr)
  count = [0] * (max_val + 1)

  while len(arr) > 0:
    num = arr.pop(0)
    count[num] += 1

  for i in range(len(count)):
    while count[i] > 0:
      arr.append(i)
      count[i] -= 1

  return arr

mylist = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
mysortedlist = countingSort(mylist)
print(mysortedlist)
