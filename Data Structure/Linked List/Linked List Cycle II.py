# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None
        start=head
        rabbit=head
        tor=head
        
        rabbit=rabbit.next.next
        tor=tor.next
        while rabbit!=tor and rabbit and  rabbit.next:
            rabbit=rabbit.next.next
            tor=tor.next
        if (not rabbit) or (not rabbit.next):
            return None
        tor=start
        while rabbit!=tor:
            rabbit=rabbit.next
            tor=tor.next
        return rabbit
        
