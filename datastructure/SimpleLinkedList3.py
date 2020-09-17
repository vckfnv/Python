class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class SimpleLinkedList:
    def __init__(self):
        head = Node('head')
        self.head = head
        self.tail = head
        self.size = 0
        
    def tailinsert(self,data):
        innode = Node(data)
        self.tail.next = innode
        self.tail = innode
        self.size += 1
        
    def headinsert(self,data):
        innode = Node(data)
        innode.next=self.head.next
        self.head.next=innode
        self.size += 1

    def headdelete(self):
        if self.size == 0:
            print("no data")
            return False
        else:
            delnode = self.head.next
            self.head.next=delnode.next
            self.size -= 1
            
    def taildelete(self):
        if self.size == 0:
            print('no data')
        else:
            delnode = self.tail
            delnode.data = None
            self.size -= 1
            
    def search(self,data):
        curr = self.head
        for i in range(self.size):
            if curr.next.data == data:
                print(data," is ",i+1,"th in list")
                return None
            curr=curr.next
        print(data,"is not in this list")
        return None

    def listnum(self):
        print("for now, there are ",self.size," elements")
        

    def printlist(self):
        curr = self.head
        if self.size == 0:
            print("no data")
            return None
        print('head::',end='')
        for i in range(self.size-1):
              print(curr.next.data,"->",end='')
              curr = curr.next
        print(curr.next.data)


list = SimpleLinkedList()
list.tailinsert(1)
list.tailinsert(2)
list.tailinsert(5)
list.tailinsert(3)
list.printlist()
list.headdelete()
list.printlist()
list.search(5)
list.headinsert(6)
list.printlist()
list.taildelete()
list.printlist()
list.listnum()
