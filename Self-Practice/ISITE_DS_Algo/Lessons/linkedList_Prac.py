import os
os.system('cls')

class Node1():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList1():
    def __init__(self):
        self.head = Node(None) # Dummy node as head
        self.size = 0
    
    def traverseList(self):
        current = self.head.next
        list = ""
        while current != None:
            list += str(current.value)
            current = current.next
            if current != None:
                list += " -> "
        print(list)

    def insertFront(self, value):
        """Inserting into the beginning of the linkedList"""
        newNode = Node(value)
        firstNode = self.head.next
        self.head.next = newNode
        newNode.next = firstNode
        
        self.size += 1
    
    def insertEnd(self, value):
        """Inserting into the end of the linkedList"""
        newNode = Node(value)
        current = self.head
        
        while current.next != None:
            current = current.next
        
        current.next = newNode
        self.size += 1
    
    def insertAtPos(self, value, pos):
        """Inserting new node into the given position"""
        newNode = Node(value)

        current = self.head
        index = 1
        while index < pos and current != None:
            current = current.next
            index += 1
        
        if current != None:
            hold = current.next
            current.next = newNode
            newNode.next = hold
            self.size += 1
            
    
    def deleteFront(self):
        """Deletes the beginning node"""
        firstNode = self.head.next

        if firstNode != None:
            self.head.next = firstNode.next
            self.size -= 1
    
    def deleteEnd(self):
        prev = self.head
        current = self.head.next

        if current != None:
            while current.next != None:
                prev = current
                current = current.next
            prev.next = None
            self.size -= 1
    
    def deleteAtPos(self, pos):
        """Deletes the node at the given position"""
        current = self.head
        index = 1
        while index < pos and current != None:
            current = current.next
            index += 1
        
        if current != None:
            current.next = current.next.next
            self.size -= 1

class Node2():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList2():
    def __init__(self):
        self.head = Node(None) # Dummy head
        self.size = 0
    
    def traverseList(self):
        """Returns the list in string format"""
        current = self.head.next
        list = ""
        while current != None:
            list += str(current.value)
            current = current.next
            if current != None:
                list += " -> "
        
        print(list)

    def insertFront(self, value):
        """Creates new node with the given value and inserts it at the beginning of the list"""
        self.insertAtPos(value, 1)
    
    def insertEnd(self, value):
        """Creates new node with the given value and inserts it at the end of the list"""
        self.insertAtPos(value, self.size + 1)
    
    def insertAtPos(self, value, position):
        """Creates a new node with the given value and inserts it at the given position"""
        newNode = Node(value)
        current = self.head
        
        index = 1
        while index < position and current != None:
            current = current.next
            index += 1
        
        if current != None:
            hold = current.next
            current.next = newNode
            newNode.next = hold
            self.size += 1
    
    def deleteFront(self):
        self.deleteAtPos(1)
    
    def deleteEnd(self):
        self.deleteAtPos(self.size-1)
    
    def deleteAtPos(self,position):
        current = self.head
        index = 1
        while index < position and current != None:
            current = current.next
            index += 1
        
        if current != None:
            current.next = current.next.next
    
    def removeElements(self, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        first = self.head
        current = self.head.next
        while current != None:
            if current.value == val:
                first.next = current.next
            first = current
            current = current.next
            

        self.traverseList()

class Node():
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def traverseList(self):
        itr = self.head
        str_list = ""
        while itr:
            str_list += str(itr.value)
            itr = itr.next
            if itr:
                str_list += " -> "
        
        print(str_list)
    
    def traverseBack(self):
        current = self.tail
        str_list = ""
        while current != None:
            str_list += str(current.value)
            current = current.prev
            if current:
                str_list += " -> "
        
        print(str_list)

    
    def insertFront(self, value):
        hold = self.head
        newNode = Node(value)
        if hold == None:
            self.head = newNode
            newNode.next = hold
        else:
            self.head = newNode
            newNode.next = hold
            hold.prev = newNode
        self.size += 1
    
    def insertEnd(self, value):
        newNode = Node(value)
        itr = self.head
        if itr is None:
            self.head = newNode
            self.tail = newNode
        else:
            while itr.next:
                itr = itr.next
            itr.next = newNode
            newNode.prev = itr
            self.tail = newNode
        self.size += 1
    
    def insertAtPos(self, value, pos):
        newNode = Node(value)
        if pos < 0 or pos > self.size+1:
            raise Exception("Index out of range")
        elif pos == 0:
            self.insertFront(value)
        elif pos == self.size+1:
            self.insertEnd(value)
        else:
            count = 0
            itr = self.head
            while count < pos - 1:
                itr = itr.next
                count += 1
            hold = itr.next
            itr.next = newNode
            newNode.next = hold
            newNode.prev = itr
            hold.prev = newNode
            self.size += 1
    
    def deleteFront(self):
        if self.head == None:
            raise Exception("Linked List is Empty")
        else:
            self.head = self.head.next
            self.size -= 1
    
    def deleteEnd(self):
        current = self.head
        itr = current.next
        if current == None:
            raise Exception("Linked List is Empty")
        elif self.head.next == None:
            self.head = None
        else:
            while itr.next:
                current = itr
                itr = itr.next
            current.next = None
        self.size -= 1
    
    def deleteAtPos(self, pos):
        prev = None
        current = self.head
        ahead = current.next
        if pos >= self.size or pos < 0:
            raise Exception("Index out of range")
        if pos == 0:
            self.deleteFront()
        else:
            counter = 0
            while counter < pos and ahead:
                prev = current
                current = ahead
                ahead = ahead.next
                counter += 1
            prev.next = ahead
            self.size -= 1
    
    def removeElements(self, value):
        first = self.head
        current = self.head.next
        if first.value == value:
            self.head = self.head.next
        while current != None:
            if current.value == value:
                first.next = current.next
            first = current
            current = current.next

    def insertAfter(self, value, after_value):
        current = self.head
        while current != None and current.value != after_value:
            current = current.next
        if current.value == after_value:
            hold = current.next
            current.next = Node(value, hold)

    def createList(self, list_val):
        self.head = None
        for i in list_val:
            self.insertEnd(i) 

print("Initialized the list with 10 values:")
newList = LinkedList()
for i in range(10):
    newList.insertEnd(i)
newList.traverseList()
newList.traverseBack()

# print()
# print("Inserting 20 at the beginning of the list:")
# newList.insertFront(20)
# newList.traverseList()


# print()
# print("Inserting 6 at the end of the list:")
# newList.insertEnd(6)
# newList.traverseList()

# print()
# print("Inserting 7 at the end of the list:")
# newList.insertEnd(7)
# newList.traverseList()

# print()
# print("Inserting 6 at the end of the list:")
# newList.insertEnd(6)
# newList.traverseList()

# print()
# print("Inserting 7 at the end of the list:")
# newList.insertEnd(7)
# newList.traverseList()

# print()
# print("Inserting 4 at index 2 of the list:")
# newList.insertAtPos(4,2)
# newList.traverseList()

# print()
# print("Inserting 1 at index 0 of the list:")
# newList.insertAtPos(1,0)
# newList.traverseList()

# print()
# print("Inserting 25 at index 17 of the list:") # Will be placed at the end because list is size 17
# newList.insertAtPos(25,17)
# newList.traverseList()

# print()
# print("Deleting the beginning node:")
# newList.deleteFront()
# newList.traverseList()

# print()
# print("Deleting the beginning node:")
# newList.deleteFront()
# newList.traverseList()

# print()
# print("Deleting the end node:")
# newList.deleteEnd()
# newList.traverseList()

# print()
# print("Deleting the node at index 2:")
# newList.deleteAtPos(2)
# newList.traverseList()

# print()
# print("Deleting the node at index 0:")
# newList.deleteAtPos(0)
# newList.traverseList()

# print()
# print("Deleting the node at index 12:")
# newList.deleteAtPos(12)
# newList.traverseList()

# print()
# print("Deleting all node with value of 6:")
# newList.removeElements(6)
# newList.traverseList()

# print()
# print("Deleting the end node:")
# newList.deleteEnd()
# newList.traverseList()

# print()
# print("Insert after first node with value of 3:")
# newList.insertAfter(11,9)
# newList.traverseList()

# print()
# print('Create new LinkedList by inputting ["banana","mango","grapes","orange"]:')
# newList.createList(["banana","mango","grapes","orange"])
# newList.traverseList()

# newList.insertAfter("apple","mango") # insert apple after mango
# newList.traverseList()
# newList.removeElements("orange") # remove orange from linked list
# newList.traverseList()
# newList.removeElements("figs")
# newList.traverseList()
# newList.removeElements("banana")
# newList.removeElements("mango")
# newList.removeElements("apple")
# newList.removeElements("grapes")
# newList.traverseList()
