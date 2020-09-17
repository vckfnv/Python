class Stack:
    def __init__(self):
        self.top=-1
        self.s=[]
        self.stacksize=0
        
    def push(self,a):
        self.s.append(a)
        self.top=self.top+1
        self.stacksize+=1

    def pop(self):
        if self.stacksize==0:
            print('nothing to pop')
        else:
            temp=self.s[self.top]
            self.s.pop()
            self.top-=1
            self.stacksize-=1
            return temp
            
    def stackprint(self):
        print(self.s)

    def peek(self):
        print(self.s[self.top])


sp=Stack()
sent3=input('후위:')
calc=['+','-','*','/']
pare=[')',']','}']
pare2=['(','{','[']
hlong3=len(sent3)
def calctwoword(x,y,z):
    
        
    if y== '+':
        return x+z
    if y=='*':
        return x*z
    if y=='-':
        return x-z
    if y=='/':
        return x/z
    
for i in range(hlong3):
    if sent3[i] in calc:
        a=int(sp.pop())
        b=int(sp.pop())
        c=calctwoword(b,sent3[i],a)
        sp.push(c)
    else:
        sp.push(sent3[i])
a=sp.pop()
print(a)
