class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class Stack():
    def __init__(self):
        self.head = Node(None)
        self.size = 0
    
    def push(self,value):
        newNode = Node(value)
        hold = self.head.next 
        self.head.next = newNode
        newNode.next = hold

        self.size += 1
    
    def pop(self):
        last = self.head.next
        self.head.next = last.next
        
        self.size -= 1

        return last.value
    
    def __str__(self) -> str:
        current = self.head.next
        vals = ""
        while current != None:
            vals += str(current.value)
            current = current.next
            if current != None:
                vals += " -> "
        
        return vals

newStack = Stack()
for i in range(10):
    newStack.push(i)
print(newStack)

for _ in range(5):
    newStack.pop()
    print(newStack)