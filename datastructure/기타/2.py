class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Stack:
    def __init__(self):
        hdnode=Node(None)
        self.head=hdnode
        self.top=hdnode
        self.stacksize=0
    def push(self,data):
        newnode=Node(data)
        if self.head.next==None:
            self.head.next=newnode
            self.top=newnode
            self.stacksize+=1
        else:
            newnode.next=self.top
            self.head.next=newnode
            self.top=newnode
            self.stacksize+=1
            
    def pop(self):
        if self.head.next==None:
            print('nothing to pop')
        else:
            temp=self.top.data
            self.top=self.top.next
            self.head.next=self.top
            self.stacksize-=1
            return temp
        
    def sprint(self):
        if self.stacksize==0:
            print("nothing in stack")
        else:
            temp=self.top
            for i in range(self.stacksize):
                
                print(temp.data,end='')
                temp=temp.next
            print()

    def peek(self):
        print(ss.top.data)

ss=Stack()

sent=input('괄호검사를 위한 식을 작성해주세요: ')
hlong=len(sent)
for i in range(hlong):
    if sent[i]=='(':
        ss.push('(')
    if sent[i]=='[':
        ss.push('[')

    if sent[i]==')':
        temp=ss.top
        if ss.stacksize==0:
            ss.push('wrong')
        else:
            if temp.data=='(':
                ss.pop()
            
    if sent[i]==']':
        temp=ss.top
        if ss.stacksize==0:
            ss.push('wrong')
        else:
            if temp.data=='[':
                ss.pop()

if ss.stacksize==0:
    print('good')
else:
    print('something wrong')

sss=Stack()
sent2=input('중위표기법:')
hlong2=len(sent2)
calc=['+','-','*','/']
pare=[')',']','}']
pare2=['(','{','[']

for i in range(hlong2):
    if sent2[i] in calc:
        sss.push(sent2[i])
        #print(sss.s)
    elif sent2[i] in pare:
        a=sss.pop()
        print(a,end='')
        #print(sss.s)
    elif sent2[i] not in pare2:
        print(sent2[i],end='')
        #print(sss.s)
    
while sss.stacksize>0:
            a=sss.pop()
            print(a)
print()

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



     
