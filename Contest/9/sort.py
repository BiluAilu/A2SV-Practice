class ListNode:
    def __init__(self,val=0,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.len = 0
        self.head = ListNode()
        self.tail = ListNode(0,self.head,None)
        self.head.next = self.tail
    def addAtIndex(self, index: int, val: int) -> None:

        if 0  <= index <= self.len:
            prev = self.find_prev(index)
            node = ListNode(val,prev,prev.next)
            prev.next.prev = node
            prev.next = node
            self.len += 1 
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.len,val)
    
def insertIntoB(b:list,value:int):
    node=ListNode()
    node.val=value
    node.prev=None
    node.next=None
    



n=int(input())
l=[]
arr=[]
for i in range(n):
    l.append(int(input()))
    arr.append(list(map(int,input().split())))

for i in range(arr):
    r=len(arr[i])-1
    b=[]

    for j in range(len(arr[i])):
        insertIntoB(b,arr[i][r])
        r-=1
    m=len(b)//2

    
    insertIntoC(b)
    arr[i].sort()
    if c==arr[i]:
        print("YES")
    else:
        print("NO")

