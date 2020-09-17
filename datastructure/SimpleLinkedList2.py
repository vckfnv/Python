class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class SimpleLinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail=head
        self.head.next=self.tail
        
    def HeadInsert(head,a):
        node = Node(a)
        node.next = head.next
        head.next = node

    def HeaedDelete(head):
        head.next=head.next.next
        

    def TailDelete(head):
        tail.data=None

    def tailinsert(head,a):
        node=Node(a)
        tail.next=node

    def Search(head,a):
        Finda = True
        while Finda == False:
            if head.next.data==a:
                Finda = True
                return head
            else:
                head=head.next

    def Insert(head,a):
        fnode=Search(head,a)
        node = Node(a)
        node.next=fnode.next
        fnode.next=node
        
    def Delete(head,a):
        fnode=Search(head,a)
        fnode.next=None
