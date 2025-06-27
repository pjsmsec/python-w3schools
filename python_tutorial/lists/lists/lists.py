mylist = ["apple", "banana", "cherry"]

print(mylist)

print()

# List items are indexed, the first item has index [0].

# List allow duplicates
thisList = ["apple", "banana", "cherry", "apple", "cherry"]

print(thisList)

print()

print(len(thisList))

print()

list1 = ["apple", "banana", "cherry"]
list2 = [1, 2, 3, 4, 5]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

for item in list4:
    print(type(item))

print()

print(type(list4))

print()

# list() constructor

newlist = list(("apple", "banana", "cherry"))

print(newlist)
