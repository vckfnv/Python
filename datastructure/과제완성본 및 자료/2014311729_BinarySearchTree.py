import random

class Node():
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

class BST():
    def __init__(self):
        self.root=Node(None)
        self.size=0
    
    def insertBST(self,bsT,x):
        newnode=Node(x)
        if bsT.data ==None:
            self.root= newnode
        else:
            fnode = bsT
            q=Node(None)
            while fnode!= None:
                if x==fnode.data:
                    print("same number!")
                q=fnode
                if x<fnode.data:
                    fnode=fnode.left
                else:
                    fnode=fnode.right
        
            if x<q.data:
                q.left=newnode  
            else:
                q.right=newnode
            self.size+=1



    def deleteBST(self,bsT,x):

        fnode=bsT
        if fnode.data==None:
            print("nothing to delete!")
        elif x==fnode.data:
            #왼쪽 서브트리의 가장 오른쪽 원소
            #자식이 2개
            if fnode.right!=None and fnode.left!=None:
                #부모노드
                parent=fnode
                #왼쪽 자식노드
                child=fnode.left
                #왼쪽 서브트리의 가장 큰 원소가 자식이 되도록.
                while child.right!=None:
                    parent=child
                    child=child.right
                #올라갈 자식노드의 오른쪽을 삭제할 노드의 오른쪽과 연결
                child.right=fnode.right
                #부모노드가 삭제할 노드인지 확인
                if parent != fnode:
                    #부모노드 오른쪽 자식은 자식노드의 왼쪽 자식이 된다.
                    #자식노드는 현재 오른쪽 자식이 없는 상태이기 때문
                    parent.right=child.left
                    child.left=fnode.left
                #fnode를 없애고 그 자리에 자식노드를 대입한다
                fnode=child
                child=None
            #만약 삭제할 노드에게 왼쪽 자식만 있을 때    
            elif fnode.right==None and fnode.left!=None:
                fnode=fnode.left
            #만약 삭제할 노드에게 오른쪽 자식만 있을 때
            elif fnode.left==None and fnode.right!=None:
                fnode=fnode.right
            #만약 삭제할 노드의 자식이 없을 때
            elif fnode.left==None and fnode.right==None:
                fnode=None
        #탐색과정    
        elif x< fnode.data:
            self.deleteBST(fnode.left,x)
        else:
            self.deleteBST(fnode.right,x)

    #중위 순회
    def printBST(self,bsT):
        if bsT != None:
            if bsT.left:
                self.printBST(bsT.left)
            print(bsT.data,end=' ')
            if bsT.right:
                self.printBST(bsT.right)

#랜덤한 10개 원소 받기
a=[]
while len(a)<10:
    randnum=random.randint(1,10)
    if randnum not in a:
        a.append(randnum)
print(a)
bst=BST()
for i in a:
    bst.insertBST(bst.root,i)
bst.printBST(bst.root)
print()
delnum=int(input("enter delete number: "))
bst.deleteBST(bst.root,delnum)
print()
bst.printBST(bst.root)
        

        
