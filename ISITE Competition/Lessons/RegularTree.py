import os
os.system('cls')

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.child = []
        self.parent = None
    
    def createChild(self, child):
        child.parent = self
        self.child.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level

    def printTree(self):
        level = self.getLevel()
        indent = "    " * level + "|--"
        if level == 0:
            print(self.value)
        else:
            print(indent + self.value)
        if self.child:
            for child in self.child:
                child.printTree()


def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode('Laptop')
    root.createChild(laptop)

    laptop.createChild(TreeNode("Asus"))
    laptop.createChild(TreeNode("Lenovo"))
    laptop.createChild(TreeNode("Dell"))

    phone = TreeNode('Mobile Phones')
    root.createChild(phone)

    phone.createChild(TreeNode('Apple'))
    phone.createChild(TreeNode('Samsung'))
    phone.createChild(TreeNode('Realme'))

    appliances = TreeNode("Appliances")
    root.createChild(appliances)

    appliances.createChild(TreeNode('Television'))
    appliances.createChild(TreeNode('Air Conditioner'))   
    appliances.createChild(TreeNode('Refrigirator'))

    root.printTree()


    return root

if __name__=='__main__':
    build_product_tree()
