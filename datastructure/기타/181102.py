class ListQueue:
    def __init__(self):
        self.qlist=[]
        self.front=-1
        self.size=0
        self.rear=self.size-1
        
        
    #def isFull(self):
        #if self.rear+1 mod self.size ==self.front
        #front=list[size]
    #def isEmpty(self):
    #    if self.front == self.rear:
    #        return True
        
    def enQ(self,data):
        
        self.qlist.append(data)
        self.size+=1
        
    def deQ(self):
        
        self.front +=1
        delnum=self.qlist[self.front]
        self.qlist=self.qlist[self.front:self.rear+1]    
        self.size-=1
        return delnum
    
    def qprint(self):
        print(self.qlist)
l=ListQueue()
l.enQ(1)
l.enQ(2)
l.deQ()
l.qprint()
