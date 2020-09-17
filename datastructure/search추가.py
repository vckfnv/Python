class Node:
    def __init__(self, data, llink = None, rlink = None):
        self.data = data
        self.llink = llink
        self.rlink = rlink

def Search(head,a):
    while True:
            if head.rlink.data >= a:
                return head.rlink
                break
            else:
                head = head.rlink

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
            
def Insert(head,x):
    node=Node(x)
    fnode=Search(head,x)
    fnode.llink.rlink=node
    node.llink=fnode.llink
    fnode.llink=node
    node.rlink=fnode
    


def Delete(head):
    while True:
        if head.rlink == None:
            head=head.llink
            head.rlink = None
            break
        else:
            head=head.rlink
            

#fnode=search(head,2)
#print("Find node = ",fnode.data)

#맨끝에 삽입 삭제하는것 과제
            
head=Node(None)
Insert(head,2)
Insert(head,1)
Insert(head,4)
Insert(head,6)
Insert(head,8)
ListPrint(head)
Delete(head)
Delete(head)
Delete(head)
Delete(head)
Delete(head)

ListPrint(head)

