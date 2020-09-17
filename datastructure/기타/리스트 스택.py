
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

#괄호검사
ss=Stack()

calc=['+','-','*','/']
pare=[')',']','}']
pare2=['(','{','[']

sent=input('괄호검사:')
hlong=len(sent)
for i in range(hlong):
    if sent[i] in pare2:
        ss.push(sent[i])
    if sent[i] in pare:
        if ss.stacksize==0:
            ss.push('wrong')
        else:
            if sent[i]==')':
               if ss.s[ss.top]=='(':
                   ss.pop()
            if sent[i]==']':
               if ss.s[ss.top]=='[':
                   ss.pop()

            if sent[i]=='}':
               if ss.s[ss.top]=='{':
                   ss.pop()
           
if ss.stacksize==0:
    print('잘했음')
else:
    print('something wrong')


#중위를 후위로~
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

#후위계산법~
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




















