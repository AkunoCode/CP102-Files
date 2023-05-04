# Linked list is a linear data type structure. Includes a series of interconnected nodes.
# Linked list are more memory efficient than a normal list in python.

class Node():
	def __init__(self):
		self.value = 0
		self.next = None

linkedList = Node()

node1 = Node()
node1.value = 5

linkedList.next = node1

node2 = Node()
node2.value = 10

node1.next = node2

# Basic Operations on Linked List
# Traversal: To traverse all the nodes one after annother.
# Insertion: To add a node at the given position.
# Deletion: To delete a node.
# Searching: To search an element(s) by value.


# TRAVERSAL OPERATION
def display(linkedList):
    current = linkedList.next
	
    # Will print the value and then move on to the next until the Node.next value becomes None
    while current != None:
        print(current.value, end=' ')
        current = current.next

# INSERT OPERATION
# Insert Operation creates a new node ad connecting it to existing nodes inside the list.
# You can insert elements to either the front, middle, or end of the linked list.

def insertFront(linkedList, newValue):
    """Creates a newNode with the given value and inserts
    it at thebeginning of the LinkedList."""  
    # Creating the newNode and assigning the given value as its value.
    newNode = Node()
    newNode.value = newValue

    # Getting the current beginning node.
    firstNode = linkedList.next

    # Replacing the beginning node with the newNode.
    linkedList.next = newNode

    # Connecting the old beginning node as the next node of the new beginning node (newNode)
    newNode.next = firstNode

print("Current linkedList:")
display(linkedList=linkedList)

# Inserting value at the beginning of the linkedList
insertFront(linkedList=linkedList, newValue=5)

print("New linkedList")
display(linkedList=linkedList)

def insertEnd(linkedList, newValue):
    """Creates a newNode with the given value and Traverse 
    till the end of the linkedList and inserts the value at the end"""
    # Creating newNode and assigning the given value as its value.
    newNode = Node()
    newNode.value = newValue

    # Traversing to the end of the linkedList and inserting the newNode as the Node.next of the formerly last Node.
    current = linkedList

    while current.next != None:
        current = current.next
    
    current.next = newNode

def insertAtPos(linkedList, newValue, pos):
    """Creates a newNode with the given value,
    Traverse the list until the index before the given pos,
    Hold the next value of that index (the current value in the given pos),
    Insert the newNode into that pos and then connect the previous value of that pos
    as the next value of the newNode."""
    newNode = Node()
    newNode.value = newValue

    current = linkedList

    index = 0
    while index < pos and current != None:
        current = current.next
        index += 1
    
    if current != None:
        hold = current.next
        current.next = newNode
        newNode.next = hold


# DELETE OPERATION
def deleteFront(linkedList):
    """Checks if the first Node is not None and replace it with the value of the next Node"""
    firstNode = linkedList.next

    if firstNode != None:
        linkedList.next = firstNode.next

def deleteEnd(linkedList):
    """Replaces the last Node with None"""
    # Creates variables that'll be used to compare
    prev = linkedList
    current = linkedList.next

    # Checks if the first value is not None
    if current != None:
        # While the next next value is not None
        # keep on moving the prev and current values until theres no more next next value
        # then replace the last node with None
        while current.next != None:
            prev = prev.next
            current = current.next
        prev.next = None
        
        # Example: 0 -> (4) -> <1> -> [2]
        # () - prev
        # <> - current
        # [] - current.next
        # If it moves one more position the current.next will be None, that'll end the loop
        # We will then replace the prev.next which will be the value of 2 into None, essentially deleting it.

def deleteAtPos(linkedList, pos):
    """Deletes nodes in the given pos"""
    current = linkedList

    index = 0
    while index < pos and current != None:
        current = current.next
        i += 1
    
    if current != None:
        hold = current.next
        current.next = hold.next




