class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#1
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, current_node, key):
        if self.root == None:
            self.root = Node(key)
        elif not self.search(self.root,key):
            if current_node.key > key:
                if current_node.left !=None:
                    self.insert(current_node.left, key)
                else:
                    current_node.left = Node(key)
                
            elif current_node.key < key:
                
                if current_node.right !=None:
                    self.insert(current_node.right,key)
                else:
                    current_node.right = Node(key)
                
    
    def search(self,current_node, key):
        if self.root == None:
            return False
        elif current_node.key ==key:
            return current_node
        elif current_node.key > key and current_node.left:
            self.search(current_node.left, key)
        elif current_node.key < key and current_node.right:
            self.search(current_node.right, key)

    def preorder(self, node):
        if node.key !=None:
            print(node.key)
            if node.left !=None:
                self.preorder(node.left)
            if node.right !=None:
                self.preorder(node.right)
bts = BinarySearchTree()
bts.insert(bts.root,15)
bts.insert(bts.root,7)
bts.insert(bts.root,22)
bts.insert(bts.root,18)

bts.insert(bts.root,10)

bts.insert(bts.root,12)

bts.preorder(bts.root)
