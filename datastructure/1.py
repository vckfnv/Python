
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

head = Node(None)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
head.next = node1
node1.next = node2
node2.next = node3

def IsHead(head):
    if head.data == None:
        print("")
        
    else:
        print(head.data)
    
        
def LinkedListPrint(head):
    while True:
        if head.next == None:
            print(head.data)
            
            break


            
        else :
            IsHead(head)
            head=head.next
LinkedListPrint(head)            
            
