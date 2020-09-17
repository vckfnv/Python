class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next

head=Node(None)
node1=Node(1)
node2=Node(2)
node3=Node(3)
head.next=node1
node1.next=node2
node2.next=node3

List=[]
#List1=[head,node1,node2,node3]
#for i in range(1,4):
#    List.append(List1[i].data)
#print(List)

def LinkedListPrint(a):
    print(a.data)
    a=a.next
    
LinkedListPrint(head)
    
