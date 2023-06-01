# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if  head==None or head.next==None or k==0:
            return head
        fast=head
        slow=head
        temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next
        
        k=k%length
        if k==0:
            return head
        for i in range(k):
            fast=fast.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        temp=slow.next
        slow.next=None
        fast.next=head
        
        return temp