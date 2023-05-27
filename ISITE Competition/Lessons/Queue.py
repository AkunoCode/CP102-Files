# Queue are FIFO (First In First Out) data structure.
# There are two basic operations that can be performed on a queue:
# 1. Enqueue: Adds an element to the end of the queue.
# 2. Dequeue: Removes the element from the front of the queue.

# You can implement a queue using a linked list. There are two ways to do this:
# 1. Enqueue at the end of the linked list and dequeue at the beginning of the linked list.
# 2. Enqueue at the beginning of the linked list and dequeue at the end of the linked list.

class Node:
    def __init__(self):
        self.value = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        newNode = Node()
        newNode.value = value

        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
    
    def dequeue(self):
        if self.head == None:
            print("Queue is empty.")
        else:
            self.head = self.head.next

    def display(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
    
    def peek(self):
        if self.head == None:
            print("Queue is empty.")
        else:
            print(self.head.value)
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

# Creating a queue
queue = Queue()

# Enqueueing values
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

# Displaying the queue
queue.display()

# Dequeueing values
queue.dequeue()
queue.dequeue()

# Displaying the queue
queue.display()

# Peeking the queue
queue.peek()

# Checking if the queue is empty
print(queue.isEmpty())

# Dequeueing values
queue.dequeue()
queue.dequeue()
queue.dequeue()

# Displaying the queue
queue.display()

# Checking if the queue is empty
print(queue.isEmpty())


# Queue can also be implemented using the built-in deque class from the collections module.
# The deque class is a double-ended queue, which means that you can enqueue and dequeue from both ends.
# The enqueue and dequeue operations are O(1) time complexity operations.

from collections import deque

# Creating a queue class
class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        self.queue.popleft()
    
    def display(self):
        print(self.queue)
    
    def peek(self):
        print(self.queue[0])
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    
# Creating a queue
queue = Queue()

# Enqueueing values
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

# Displaying the queue
queue.display()

# Dequeueing values
queue.dequeue()
queue.dequeue()

# Displaying the queue
queue.display()

# Peeking the queue
queue.peek()

# Checking if the queue is empty
print(queue.isEmpty())

# Dequeueing values
queue.dequeue()
queue.dequeue()
queue.dequeue()

# Displaying the queue
queue.display()

# Checking if the queue is empty
print(queue.isEmpty())

