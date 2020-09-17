#이중연결리스트
#Node class
class Node:
    def __init__(self, data, llink = None, rlink = None):
        self.data = data
        self.llink = llink
        self.rlink = rlink
#Listprint function
def ListPrint(head):
    while True:
        
        if head.rlink == None:
            if head.data == None:
                print("no data")
            else:
                print()
            break
        else:
            head = head.rlink
            print(head.data," ",end="")
#Insert at the end           
def Insert(head,x):
    while True:
        
        if head.rlink == None:
            node=Node(x)
            head.rlink=node
            node.llink=head
            
            

            break
        else:
            head=head.rlink

#Delete at the end
def Delete(head):
    while True:
        if head.rlink == None:
            head=head.llink
            head.rlink = None
            break
        else:
            head=head.rlink
            
#Insertion and Deletion
head=Node(None)
Insert(head,2)
Insert(head,1)
Insert(head,4)
Insert(head,6)
Insert(head,8)
ListPrint(head)
for i in range(5):
    Delete(head)
    ListPrint(head)
