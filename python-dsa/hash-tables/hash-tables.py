# Hash table

# A hash table is a data structure desinged to be fast to work with

# Building a hash table from scratch
my_list = [None, None, None, None, None, None, None, None, None, None]
# Note: each of these elements is called a bucket in a hash table

# Create a hash function
def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

print("'Bob' has a hash code:", hash_function('Bob'))

print()

# Inserting an element
def add(name):
    index = hash_function(name)
    my_list[index] = name

add('Bob')
print(my_list)

print()

add('Pete')
add('Jones')
add('Lisa')
add('Siri')
print(my_list)

print()

# Looking up a name
def contains(name):
    index = hash_function(name)
    return my_list[index] == name

print("'Pete' is in the Hash Table:" , contains('Pete'))

print()

# Handling collisions
my_list = [
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  []
]

def add(name):
  index = hash_function(name)
  my_list[index].append(name)

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')
print(my_list) 
