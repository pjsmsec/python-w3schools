# + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

print(list3)

print()

for x in list2:
    list1.append(x)

print(list1)

print()

# The extend() method adds elements from one list to another
list1.extend(list2)

print(list1)
