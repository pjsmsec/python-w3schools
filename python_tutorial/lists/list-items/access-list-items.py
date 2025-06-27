thislist = ["apple", "banana", "cherry"]

print(thislist[1])

print()

# Negative indexing
# -1 refers to the last item
print(thislist[-1])

print()

# Range of indexes
newlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(newlist[2:5])
# Lists' indexes are 0 based
# The first value of the range is inclusive and the second is exclusive

print()

print(newlist[:4])
# Not including the first value indexes from the beginning of the list

print()

print(newlist[2:])
# Not inclusing the last value indexes till the list's end

print()

# Range of negative indexes
print(newlist[-4:-1])

print()

# Check if item exists in list
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
