class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class SimpleLinkedList:
    def __init__(self):
        head = Node('head')
        self.head = head 
        self.tail = head 
        
        
    def tailinsert(self,data):
        innode = Node(data)
        self.tail.next = innode
        self.tail = innode
        
        
    def headinsert(self,data):
        innode = Node(data)
        innode.next=self.head.next
        self.head.next=innode
        

    def headdelete(self):
        if self.head.next == None:
            print("no data")
            
        else:
            delnode = self.head.next
            self.head.next=delnode.next
            
    def taildelete(self):
        
        if self.head.next == None:
            print('no data')
        else:
            self.tail=None
            
            

    def printlist(self):
        curr = self.head
        while True:
            
            if curr.next==None:
                print(curr.data,end='')
                break
            else:
                if curr.data=='head':
                    print('')
                    curr=curr.next
                else:    
                    print(curr.data,end='')
                    curr=curr.next
                
        
    def search(self,data):
        curr = self.head
        flag =False
        while flag == False:
            
            if curr.data == data:
                return curr
                flag =True
            else:
                if curr.next == None:
                    flag =True
                else:
                    curr=curr.next

    def insertafter(self,data):
        node=Node(data)
        fnode= self.search(data)
        node.next=fnode.next
        fnode.next=node

        
list = SimpleLinkedList()
list.tailinsert(1)
list.tailinsert(2)
list.tailinsert(5)
list.tailinsert(3)
list.printlist()
list.headdelete()
list.printlist()
list.headinsert(6)
list.printlist()
list.taildelete()
list.printlist()
list.tailinsert(7)
list.printlist()
print(list.search(2).data)
list.insertafter(2)
