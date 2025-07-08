# Linear Search

# Steps:
# 1 - Go through the array value by value from the start.
# 2 - Compare each value to check if it is equal to the value we are looking for.    
# 3 - If the value is found, return the index of that value.
# 4 - If the end of the array is reached and the value is not found, return -1 to 
#   indicate that the value was not found.

mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]

if 4 in mylist:
    print("Found!")
else:
    print("Not found!")

print()

def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
        return -1

mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]
x = 4

result = linearSearch(mylist, x)

if result != -1:
    print("Found at index", result)
else:
    print("Not found")
