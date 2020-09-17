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
            
class SimpleLinkedList:
    def __init__(self,head):
        head = Node(None)
        self.tail=head
        self.tail.next=None
        
    def Insert(node):
        
        node.next=head.next
        head.next=node

    def delete():
        head.next=node.next

    def search(head):
        i=1
        while True:
            if head.next == None:
                print(head.data)
                a=str(i-1)
                bb=print(a+"번째")
                return i-1

                break
            else:
                IsHead(head)
                head=head.next
                i+=1
            
    def delete2():
        n=search(head)
        
node=Node(4)
SimpleLinkedList.Insert(node)
print("insert 4")
LinkedListPrint(head)
SimpleLinkedList.delete()
print("delete head.next")
LinkedListPrint(head)
SimpleLinkedList.search(head)
SimpleLinkedList.delete2()
LinkedListPrint(head)
