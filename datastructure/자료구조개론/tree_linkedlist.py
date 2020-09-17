class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        

class Tree:
    def __init__(self):
        self.head=Node(None)
        self.size=0
        self.root=self.head
    
    def insert(self,data):
        newnode=Node(data)
        #root node
        if self.size==0:
            self.head.next=newnode
            self.root=newnode
            self.size+=1
        else:
            
            findnode=self.search(self.root,data)
            if findnode.data < data:
                findnode.right = newnode
                self.size+=1
            if findnode.data > data:
                findnode.left = newnode
                self.size+=1
    def search(self,T,data):
        if T.data != None:
            if T.data < data:
                if T.right ==None:
                    return T
                else:
                    self.search(T.right,data)
            if T.data > data:
                if T.left == None:
                    return T
                else:
                    self.search(T.left,data)
       
    def showTree(self,ro):
        if ro.data == None:
            print()
        else:
            
            print(ro.data)
            self.showTree(ro.left)
            self.showTree(ro.right)
        

tt=Tree()
tt.insert(5)
tt.insert(3)
tt.insert(1)
tt.showTree(tt.root)
