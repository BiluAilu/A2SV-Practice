# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result=[]
        c=0
        while l1 and l2:
            r=l1.val+l2.val+c
            if r>=10:
                m=r%10
                result.append(m)
                c=1

                
            else:
                result.append(l1.val+l2.val+c)
                c=0

            l1=l1.next
            l2=l2.next
        if l1:
            while l1:
                if l1.val+c<10:
                    result.append(l1.val+c)
                    c=0
                else:
                    result.append((l1.val+c)%10)
                    c=1
                l1=l1.next
        elif l2:
            while l2:
                if l2.val+c<10:
                    result.append(l2.val+c)
                    c=0
                else:
                    result.append((l2.val+c)%10)
                    c=1
                l2=l2.next
        if c==1:
            result.append(1)
        result[0]=ListNode(result[0],None)
        myList=ListNode(0,result[0])
        for i in range(1,len(result)):
            result[i]=ListNode(result[i],None)
            result[i-1].next=result[i]
        return myList.next
                


