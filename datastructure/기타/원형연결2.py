class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class CLL:
    def __init__(self):
        hdnode=Node(None)
        self.head=hdnode
        self.size=0

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
                    #헤드다음들어갈때
                    if self.head.next==temp:    
                        for i in range(self.size-1):
                            temp=temp.next
                        newnode.next=self.head.next
                        temp.next=newnode
                        self.head.next=newnode
                        self.size+=1
                        break
                    else:
                        #가운데 들어갈때
                        newnode.next=temp
                        prev.next=newnode
                        self.size+=1
                        break
                else:
                    #제일 끝에들어갈때
                    if temp.next==self.head.next:
                        prev=temp
                        prev.next=newnode
                        newnode.next=self.head.next
                        self.size+=1
                        break
                    else:
                        #이동
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
                        self.size-=1
                        break
                    elif temp.next==self.head.next:
                        prev.next=temp.next
                        self.size-=1
                        break
                    else:
                        prev.next=temp.next
                        self.size-=1
                        break
                else:
                    if temp.next==self.head.next:
                        break
                    else:
                        prev=temp
                        
                


                
    def print(self):
        temp=self.head
        for i in range(self.size):
            temp=temp.next
            print(temp.data," ",end='')
        print()


a=CLL()
a.insertmid(2)
a.insertmid(4)
a.insertmid(3)
#temp=a.head
#for i in range(a.size+1):
#    temp=temp.next
#    print(temp.data)
#print(temp.data)
a.insertmid(15)
a.insertmid(1)
a.print()
a.delete(2)
a.print()
#a.delete(1)
#a.print()
a.delete(15)
a.print()
