class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class QQ:
    def __init__(self):
        
        self.head=Node(None)
        self.size=0
        
    def insert(self,data):
        newnode=Node(data)
        if self.size==0:
            self.head.next=newnode
            self.size+=1
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
            self.size+=1

        
    def delete(self):
        temp=self.head.next
        self.head.next=temp.next
        self.size-=1
        


    
    def showme(self):
        temp=self.head
        for i in range(self.size):
            temp=temp.next
            print("[",temp.data,"] ",end='')
        print()
qq=QQ()
qq.insert(1)
qq.insert(3)
qq.insert(5)
qq.insert(2)
qq.showme()
qq.delete()
qq.showme()
