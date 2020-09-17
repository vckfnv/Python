class Node:
        def __init__(self,data,next=None):
            self.data=data
            self.next=next

class SimpleLinkedList:
    
    #Initialize method 
    def __init__(self):
        hdnode=Node(None)
        self.head=hdnode
        self.count=0
        self.curr=hdnode
        self.prev=hdnode
        
    #Insertion
    def Insert(self,data):
        
        #Create new node
        newnode = Node(data)
        
        #Insert at first
        if self.count == 0:
            self.head.next = newnode
            self.count += 1
            
        
        else:
            
            #Find a place where data to be located
            self.Search(data)
            
            #Exception when same data is existed
            if self.curr.data==data:
                print("There are same numbers. \
Please enter 5 different numbers")
            else:
                #Insert at the end
                if self.prev.next ==None:
                    self.prev.next = newnode
                    self.count += 1
                #Insert at the middle part
                else:
                    newnode.next = self.curr
                    self.prev.next = newnode
                    self.count += 1

        #Move curr&prev to head
        self.GetBack()

    #Deletion
    def Delete(self,data):
        #If there are no elements in List
        if self.count == 0:
            print("Nothing to delete.")

        else:
            #Find a place where data to be located    
            self.Search(data)

            #Exception when there isn't same number
            if self.curr.data != data:
                print("\nCan't find the number in this List.\
 Please try again.\n")

            else:
                #Deletion    
                self.prev.next = self.curr.next
                self.count -= 1

        #Move curr&prev to head
        self.GetBack()

    #Search the place where data to be located            
    def Search(self,data):
        
        while True:
            #At first, locate curr node to be next of head
            self.curr=self.curr.next

            #Find place where data is less than curr's data
            if data <=self.curr.data:

                #When found
                break

            else:
                #When curr is at the end
                if self.curr.next == None:

                    #Move prev to curr
                    self.prev=self.curr
                    break

                #When curr is not at the end
                else:

                    #Move prev to curr
                    self.prev=self.curr

    #Print List                
    def PrintList(self):

        #When no element
        if self.count ==0:
            print("no data")
        else:
                
            print("Head",end='')
            #Print 'count' times
            for i in range(self.count):
                #Move curr to next then print
                self.curr = self.curr.next
                print(" →",self.curr.data,end='')        
            print()

        #Move curr&prev to head
        self.GetBack()

    def GetBack(self):
        self.prev=self.head
        self.curr=self.head

    def DrawLine(self):
        print("\n========================================================\n")

    def ShowList(self):
        self.DrawLine()
        self.PrintList()
        self.DrawLine()

        
sll=SimpleLinkedList()

#Input 5 elements to SimpleLinkedList
while sll.count<5:
    num=int(input("Enter number (1~100): "))
    if num<=100:
            
            sll.Insert(num)
    else:
            print("\nnumber must be less or equal to 100\n")

sll.DrawLine()
print("SimpleLinkedList with sorted numbers are created")
sll.ShowList()

while sll.count>0:
    NumOfData=sll.count
    delnum=int(input("Enter the number to be deleted in the List: "))
    sll.Delete(delnum)

    if NumOfData-1==sll.count:

        if sll.count ==0:
            sll.Delete(delnum)

        else:
            sll.ShowList()

    else:
        continue
















