class Node():
    def __init__(self,data,right=None,left=None):
        self.data=data
        self.right=right
        self.left=left

class deque():
    def __init__(self):
        self.head=Node(None)
        self.front=self.head
        self.rear=self.head
        self.size=0
    def insertFront(self,data):
        newnode=Node(data)
        if self.size==0:
            self.head.right=newnode
            self.rear=newnode
            self.front=newnode
            self.size+=1
            print("front 삽입 ",data,">>",end='')
        else:
            self.front.left=newnode
            self.head.right=newnode
            newnode.right=self.front
            newnode.left=self.head
            self.front=newnode
            self.size+=1
            print("front 삽입 ",data,">>",end='')
    def insertRear(self,data):
        newnode=Node(data)
        if self.size==0:
            self.head.next=newnode
            self.rear=newnode
            self.front=newnode
            self.size+=1
            print("rear  삽입 ",data,">>",end='')
        else:
            self.rear.right=newnode
            newnode.left=self.rear
            self.rear=newnode
            self.size+=1
            print("rear  삽입 ",data,">>",end='')
    def deleteFront(self):
        if self.size==0:
            print("nothing to delete")
            
        if self.size==1:
            self.head.right=None
            self.front=None
            self.rear=None
            self.size-=1
            print("front 삭제    >>",end='')
        else:
            curr=self.front.right
            self.head.right=curr
            curr.left=self.head
            self.front=curr
            self.size-=1
            print("front 삭제    >>",end='')
    def deleteRear(self):
        if self.size==0:
            print("nothing to delete")
        if self.size==1:
            self.head.right=None
            self.front=None
            self.rear=None
            self.size-=1
            print("Rear  삭제    >>",end='')
        else:
            curr=self.rear.left
            curr.right=None
            self.rear=curr
            self.size-=1
            print("Rear  삭제    >>",end='')

    def showUp(self):
        temp=self.head
        print(" DeQue : [ ",end='')
        for i in range(self.size):
            temp=temp.right
            print(temp.data,end=' ')
        print("]")


dq=deque()
dq.insertFront('A')
dq.showUp()
dq.insertFront('B')
dq.showUp()
dq.insertRear('C')
dq.showUp()
dq.deleteFront()
dq.showUp()
dq.deleteRear()
dq.showUp()
dq.insertRear('D')
dq.showUp()
dq.insertFront('E')
dq.showUp()
dq.insertFront('F')
dq.showUp()
