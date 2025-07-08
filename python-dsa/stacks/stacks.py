# Stacks

# A stack is a data structure that can hold many elements, and the last element 
# added is the first one to be removed (LIFO)

# Stack operations:
# Push - add a new element on the stack
# Pop - removes and returns the top element form the stack
# Peek - Returns the top (last) element on the stack
# isEmpty - Checks if the stack is empty
# Size - Finds the number of elements in the stack

# Stacks can be implemented by using arrays or linked lists

# Stack implementation using Python lists
x = [5, 6, 2, 9, 3, 8, 4, 2]

# Example
stack = []

stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

topElement = stack[-1]
print("Peek: ", topElement)

poppedElement = stack.pop()
print("Pop: ", poppedElement)

print("Stack after Pop: ", stack)

isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

print("Size: ", len(stack))

# Besides using lists, the stack class can also be used
class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)

myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())

print()

# Reasons to implement stacks using lists/arrays:

#     Memory Efficient: Array elements do not hold the next elements address like 
#       linked list nodes do.
#     Easier to implement and understand: Using arrays to implement stacks require 
#       less code than using linked lists, and for this reason it is typically 
#       easier to understand as well.

# A reason for not using arrays to implement stacks:

#     Fixed size: An array occupies a fixed part of the memory. This means that it 
#       could take up more memory than needed, or if the array fills up, it cannot 
#       hold more elements.

# Stack implementation using linked lists
# A linked list consists of nodes with some sort of data, and a pointer to the next
# node
# A big benefit with using linked lists is that nodes are stored wherever there is
# free space in memory.
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, value):
    new_node = Node(value)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size += 1

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    popped_node = self.head
    self.head = self.head.next
    self.size -= 1
    return popped_node.value

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.head.value

  def isEmpty(self):
    return self.size == 0

  def stackSize(self):
    return self.size

  def traverseAndPrint(self):
    currentNode = self.head
    while currentNode:
      print(currentNode.value, end=" -> ")
      currentNode = currentNode.next
    print()

myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("LinkedList: ", end="")
myStack.traverseAndPrint()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
myStack.traverseAndPrint()
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())
