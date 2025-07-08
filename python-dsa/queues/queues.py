# Queues
# Basic operations:
# Enqueue - Adds a new element to the queue
# Dequeue - Removes and returns the first (front) element from the queue
# Peek - Returns the first element in the queue
# isEmpty - Checks if the queue is empty
# Size - Finds the number of elements in the queue

# Queues are implemented using arrays or linked lists

x = [5, 6, 2, 9, 3, 8, 4, 2]

# Example:
queue = []

queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

frontElement = queue[0]
print("Peek: ", frontElement)

poppedElement = queue.pop(0)
print("Dequeue: ", poppedElement)

print("Queue after Dequeue: ", queue)

isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

print("Size: ", len(queue))

print()

# Implementing a queue class
class Queue:
  def __init__(self):
    self.queue = []
    
  def enqueue(self, element):
    self.queue.append(element)

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue.pop(0)

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue[0]

  def isEmpty(self):
    return len(self.queue) == 0

  def size(self):
    return len(self.queue)

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", myQueue.queue)
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", myQueue.queue)
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())

print()

# Queue implementation using linked lists
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.length = 0

  def enqueue(self, element):
    new_node = Node(element)
    if self.rear is None:
      self.front = self.rear = new_node
      self.length += 1
      return
    self.rear.next = new_node
    self.rear = new_node
    self.length += 1

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"

  def isEmpty(self):
    return self.length == 0

  def size(self):
    return self.length

  def printQueue(self):
    temp = self.front
    while temp:
      print(temp.data, end=" ")
      temp = temp.next
    print()

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    temp = self.front
    self.front = temp.next
    self.length -= 1
    if self.front is None:
      self.rear = None
    return temp.data

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.front.data

  def isEmpty(self):
    return self.length == 0

  def size(self):
    return self.length

  def printQueue(self):
    temp = self.front
    while temp:
      print(temp.data, end=" -> ")
      temp = temp.next
    print()

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", end="")
myQueue.printQueue()
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", end="")
myQueue.printQueue()
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())

