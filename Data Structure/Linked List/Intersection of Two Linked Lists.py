# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h1=p1=headA
        h2=p2=headB
        
        l1=0
        l2=0

        while p1:
            p1=p1.next
            l1+=1
        while p2:
            p2=p2.next
            l2+=1
        if(l1>l2):
            dif=l1-l2
            for i in range(dif):
                h1=h1.next
            while h1:
                if h1.val==h2.val and h1==h2:
                    return h1
                h1=h1.next
                h2=h2.next
        elif(l1<l2):
            dif=l2-l1
            for i in range(dif):
                h2=h2.next
            while h2:
                if h2.val==h1.val and h1==h2:
                    return h2
                h1=h1.next
                h2=h2.next
        else:
            while h2:
                if h2.val==h1.val and h1==h2:
                    return h2
                h1=h1.next
                h2=h2.next
        
        return None      