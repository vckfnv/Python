class Heap:
    def __init__(self):
        self.hlist=[0]
        #heap의 크기
        self.size=0
        
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
        
    def insertHeap(self, item):
        if self.size == 0:
            self.hlist.append(item)
            self.size+=1
        else:
            self.hlist.append(item)
            self.size+=1
            i=self.size
            while i>1:
                p= int(i//2)
                if self.hlist[p] < self.hlist[i]:
                    parent=self.hlist[p]
                    self.hlist[p] = self.hlist[i]
                    self.hlist[i] = parent
                    i = p
                else:
                    break
       
    def deleteHeap(self):
        if self.isEmpty ==True:
            print('nothing to delete')
        else:
            self.hlist[1]=self.hlist[self.size]
            self.hlist.pop()
            self.size-=1
            i=1
            while i<=self.size:
                
                if 2*i > self.size:
                    break
                if 2*i == self.size:
                    if self.hlist[2*i] < self.hlist[i]:
                        break
                    if self.hlist[2*i] > self.hlist[i]:
                        child = self.hlist[2*i]
                        self.hlist[2*i]=self.hlist[i]
                        self.hlist[i]=child
                else:
                    bigchild=self.comparechild(i)
                    if self.hlist[bigchild] < self.hlist[i]:
                        break
                    if self.hlist[bigchild] > self.hlist[i]:
                        child = self.hlist[bigchild]
                        self.hlist[bigchild]=self.hlist[i]
                        self.hlist[i]=child
    def comparechild(self,num):
        #자식이 0,1,2개일 때
        #자식이 없다는 조건은 2a가 numofdata보다 크면 없는거 또는 len(list)
        #자식이 1개: a*2=len(list)
        #나머지는 2개라는 것.
        if self.hlist[2*num] < self.hlist[2*num+1]:
            return 2*num+1
        if self.hlist[2*num] > self.hlist[2*num+1]:
            return 2*num
    def printHeap(self):
        
        for i in range(self.size):
            print('[',self.hlist[i+1],']',end=' ')
        print()

h=Heap()
for i in range(10):
    nums=input("Insert numbers: ")
    h.insertHeap(nums)
print("=================================================\nShow Heap:")
h.printHeap()
