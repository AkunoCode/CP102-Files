class treeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insertChild(self,val):
        if val == self.val:
            return
        if val < self.val:
            if self.left:
                self.left.insertChild(val)
            else:
                self.left = treeNode(val)
        elif val > self.val:
            if self.right:
                self.right.insertChild(val)
            else:
                self.right = treeNode(val)
        
    def sortedTraversal(self):
        elements = []
        if self.left:
            elements += self.left.sortedTraversal()
        
        elements.append(self.val)

        if self.right:
            elements += self.right.sortedTraversal()
        
        return elements
    
    def preOrdTraversal(self):
        elements = []
        elements.append(self.val)
        if self.left:
            elements += self.left.preOrdTraversal()
        if self.right:
            elements += self.right.preOrdTraversal()
        return elements
    
    def postOrdTraversal(self):
        elements = []
        if self.left:
            elements += self.left.postOrdTraversal()
        if self.right:
            elements += self.right.postOrdTraversal()
        elements.append(self.val)
        return elements
      
    
    def searchValue(self,val):
        if self.val == val:
            return True
        elif val < self.val:
            if self.left:
                return self.left.searchValue(val)
            else:
                return False
        elif val > self.val:
            if self.right:
                return self.right.searchValue(val)
            else:
                return False
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        if self.val:
            return self.val
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        
        return self.val
    
    def calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()

        sum += self.val

        if self.right:
            sum += self.right.calculate_sum()

        return sum
    

    
    
def buildBinaryTree(list_val):
    root = treeNode(list_val[0])

    for i in range(1,len(list_val)):
        root.insertChild(list_val[i])
    
    return root

if __name__ == '__main__':
    numbers = [5,3,7,1,4,6,8]
    newTree = buildBinaryTree(numbers)
    print(newTree.sortedTraversal())
    print(newTree.searchValue(5))
    print(newTree.find_min())
    print(newTree.find_max())
    print(newTree.calculate_sum())
    print(newTree.preOrdTraversal())
    print(newTree.postOrdTraversal())

