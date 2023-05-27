class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.size = 0
    
    def traverseList(self):
        current = self.head.next
        vals = ""
        while current != None:
            vals += str(current.value)
            current = current.next
            if current != None:
                vals += " -> "
        
        print(vals)
    
    def insertFront(self,value):
        newNode = Node(value)
        currenthead = self.head.next
        self.head.next = newNode
        newNode.next = currenthead
        
        self.size += 1

    def insertEnd(self,value):
        newNode = Node(value)
        current = self.head.next
        while current.next != None:
            current = current.next
        
        current.next = newNode
        self.size += 1
    
    def insertAtPos(self,value,pos):
        newNode = Node(value)
        count = 1
        current = self.head
        while count < pos:
            current = current.next
            count += 1
        
        hold = current.next
        current.next = newNode
        newNode.next = hold

        self.size += 1

    def deleteFront(self):
        self.head.next = self.head.next.next
        self.size -= 1
    
    def deleteEnd(self):
        if self.size == 1:
            self.head.next = None
        else:
            current = self.head.next
            while current.next.next != None:
                current = current.next
            
            current.next = None
        self.size -= 1

    def deleteAtPos(self,pos):
        index = 1
        current = self.head
        while index < pos:
            current = current.next
            index += 1

        hold = current.next.next
        current.next = hold

        self.size -= 1


newList = LinkedList()

newList.traverseList()
newList.insertFront(10)
newList.traverseList()
newList.insertFront(20)
newList.insertFront(30)
newList.insertFront(40)
newList.insertEnd(80)
newList.insertAtPos(5,6)
newList.traverseList()

newList.deleteFront()
newList.traverseList()

newList.deleteEnd()
newList.traverseList()

newList.deleteAtPos(2)
newList.traverseList()