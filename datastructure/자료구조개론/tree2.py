Tree=[0]

def find(a):
    while True:
        n=1
        if 2**(n-1)<=a<2**n:
            return n
        else:
            n+=1
            continue
        
def search(a,value):
    num=int(Tree[a])
    #value가 더 작을 때
    if Tree[a]>value:

        #현재 트리의 크기가 2a보다 작거나 같을 때
        if len(Tree)<=2*a:
            #2의 n제곱만큼 0을 append한다(n=find(a))
            for i in range(2**find(a)):
                Tree.append(0)
            #2a번째 위치에서 재귀
            search(a*2,value)
            
        #현재 트리의 크기가 2a보다 클 때
        else:
            #2a번째 위치에서 재귀
            search(a*2,value)
    #value가 더 클 때
    if Tree[a]<value:

        #현재 트리의 크기가 2a보다 작거나 같을 때
        if len(Tree)<=a*2:
            #2의 n제곱만큼 0을 append한다
            for i in range(2**find(a)):
                Tree.append(0)
            #2a+1번째 위치에서 재귀
            search(a*2+1,value)
        #현재 트리의 크기가 2a보다 클 때
        else:
            #2a번째 위치에서 재귀
            search(a*2+1,value)
    #현재 위치에 0이 들어있다면(비어 있음)
    if Tree[a]==0:
        #그 위치에 value를 집어넣는다.
        Tree[a]=value
        
    #그 외에는 숫자가 같을 때
    else:
        
        print('there is same number or something\'s wrong')
    

def insert(value):
    #root 넣을 때
    if len(Tree)==1:
        Tree.append(value)
    #나머지
    else:
        search(1,value)
        



        
for i in range(10):
    elements=int(input("insert number: "))
    insert(elements)
    print(Tree)
