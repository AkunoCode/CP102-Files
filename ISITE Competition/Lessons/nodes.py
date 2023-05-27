# Nodes contains data and a pointer to another node

class Node:
    def __init__(self):
        self.value = 0
        self.next = None

# Creating instances of the Node
node1 = Node()
node2 = Node()
node3 = Node()

# Assigning values to the Nodes
node1.value = 10
node2.value = 20
node3.value = 30

# Connecting the Nodes
node1.next = node2
node2.next = node3

print(f"Node 1 is pointing to Node 2 which has a value of {node1.next.value}")


# Special Type of Nodes
# Orphaned Nodes - Orphaned Nodes doesn't have parents either because they are removed or created without parent nodes.
# Null Nodes - Special value that indicates the absence of a node. Can be used to initialize or end a linkedlist.
