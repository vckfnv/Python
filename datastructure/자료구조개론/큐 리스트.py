class QQ():
    def __init__(self,n):
        self.q=[]
        self.front=0
        self.rear=0
        self.size=n
        for i in range(n):
            self.q.append(None)
    def isFull(self):
        
        if (self.rear+1)%(self.size)==(self.front) and self.q[self.rear]!=0:
            return True
        else:
            return False

    def isEmpty(self):
        if self.front==self.rear:
            return True
        else:
            return False
    def insert(self,data):
        if self.isFull():
            print("It's full, can't insert anymore")
        else:
            self.rear=(self.rear+1)%self.size
            self.q[self.rear]=(data)
            
            
          
            
            
    def delete(self):
        if self.isEmpty():
            print("nothing to delete")
        else:
            self.front=(self.front+1)%self.size
            self.q[self.front]="deleted"
            
            

    def showup(self):
        for i in range(len(self.q)):
            print(self.q[i]," ",end='')
        print()

qq=QQ(5)
qq.insert(1)
qq.insert(2)
qq.insert(3)
qq.showup()
qq.delete()
qq.showup()
qq.insert(4)
qq.showup()
qq.insert(5)
qq.showup()
qq.insert(6)
qq.showup()
