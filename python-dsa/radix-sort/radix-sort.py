# Radix sort

# Setps:
# 1 - Start with the least significant digit (rightmost digit).
# 2 - Sort the values based on the digit in focus by first putting the values in the 
#       correct bucket based on the digit in focus, and then put them back into 
#       array in the correct order.
# 3 - Move to the next digit, and sort again, like in the step above, until there 
#       are no digits left.

mylist = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", mylist)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(mylist)
exp = 1

while maxVal // exp > 0:

  while len(mylist) > 0:
    val = mylist.pop()
    radixIndex = (val // exp) % 10
    radixArray[radixIndex].append(val)

  for bucket in radixArray:
    while len(bucket) > 0:
      val = bucket.pop()
      mylist.append(val)

  exp *= 10

print(mylist) 

print()

# Radix sort using other sorting algorithms
def bubbleSort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

def radixSortWithBubbleSort(arr):
  max_val = max(arr)
  exp = 1

  while max_val // exp > 0:
    radixList = [[],[],[],[],[],[],[],[],[],[]]

    for num in arr:
      radixIndex = (num // exp) % 10
      radixList[radixIndex].append(num)

    for bucket in radixList:
      bubbleSort(bucket)

    i = 0
    for bucket in radixList:
      for num in bucket:
        arr[i] = num
        i += 1

    exp *= 10

mylist = [170, 45, 75, 90, 802, 24, 2, 66]

radixSortWithBubbleSort(mylist)

print(mylist)
