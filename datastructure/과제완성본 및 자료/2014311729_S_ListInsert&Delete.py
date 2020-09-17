#List insert delete
#2014311729_S_ListInsert&Delete.py

L1=[1,3,7,11,13,15]
#위치 찾기
def search(k):
        for i in range(len(L1)):
            if L1[i]<=k<L1[i+1]:
                idx=i
                return idx
#삽입    
def insert(k):
        num=search(k)
#리스트 끝에 삽입
        L1.append(k)
#끝에서부터 차례차례 크기비교하며 순서변경
        for i in range(1,len(L1)-num-1):
                L1[len(L1)-i]=L1[len(L1)-i-1]
                L1[len(L1)-i-1]=k
#삭제        
def delete(k):
        num=search(k)
#삭제할 숫자를 크기비교하며 순서변경 후 맨 끝으로 이동
        for i in range(len(L1)-num-1):
                L1[num+i]=L1[num+i+1]
                L1[num+i+1]=k
#제일 끝 원소 삭제
        L1.pop()
    
flag=True 
while flag == True:
    print(L1)
    a=int(input('Enter the number:'))
    b=input('insert(i) or delete(d) or quit(q)?:')
    
    
    if b=='d':
        if a in L1:
                delete(a)
        else:
                print('Not in the List. Only same number can be deleted')
    if b=='i':
        insert(a)
    if b=='q':
        flag = False

    
    

    
        
        
