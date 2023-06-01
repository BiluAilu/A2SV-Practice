# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None or head.next.next==None:
            return head
        odH=head
        temp=evH=head.next
        
        while evH.next and evH.next.next:
            odH.next=evH.next
            evH.next=evH.next.next
            odH=odH.next
            evH=evH.next
        if evH.next:
            odH.next=evH.next
            evH.next=None
            odH=odH.next
            
        odH.next=temp
        # return temp
        return head
