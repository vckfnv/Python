class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class CLL:
    def __init__(self):
        hdnode=Node(None)
        self.head=hdnode
        self.size=0
    #def insert(self,data):
    #    newnode=Node(data)
    #    if self.size==0:
    #        self.head.next=newnode
    #        newnode.next=newnode
    #        self.size+=1
    #    else:
    #        temp=self.head
    #        for i in range(self.size):
    #            temp=temp.next

    #        newnode.next=temp.next
    #        temp.next=newnode
            
    #        self.size+=1
    #def delete(self,data):

    def insertmid(self,data):
        prev=self.head
        temp=self.head
        newnode=Node(data)
        if self.size==0:
            self.head.next=newnode
            newnode.next=newnode
            self.size+=1
            
        else:
            while True:
                temp=temp.next
                if data<=temp.data:
                    if temp.next ==temp:
                        newnode.next=temp
                        prev.next=newnode
                        temp.next=newnode
                        self.size+=1
                        break

                    else:
                        for i in range(self.size-1):
                            temp=temp.next
                        newnode.next=self.head.next
                        temp.next=newnode
                        self.head.next=newnode
                        self.size+=1
                        break
                else:
                    if temp.next==temp:
                        prev=temp
                        prev.next=newnode
                        newnode.next=temp.next
                        self.size+=1
                        break
                    else:
                        prev=temp
                        continue

    def delete(self,data):
        if self.size==0:
            print('nothing to delete')

        else:
            
            temp=self.head
            prev=self.head
            while True:
                temp=temp.next
                if temp.data==data:
                    if temp==self.head.next:
                        prev.next=temp.next
                        prev=temp.next
                        for i in range(self.size-1):
                            temp=temp.next
                        temp.next=prev
                    elif temp.next==head.next:
                        prev.next=temp.next
                    else:
                        prev.next=temp.next
                else:
                    if temp.next==self.head.next:
                        break
                    else:
                        prev=temp
                        temp=temp.next
                

                
    def print(self):
        temp=self.head
        for i in range(self.size):
            temp=temp.next
            print(temp.data,end='')
        print()


a=CLL()
a.insertmid(2)
a.insertmid(4)
a.insertmid(3)
a.insertmid(15)
a.print()
a.delete(2)
