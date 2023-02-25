# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        0 1 1 1 2
        '''
        curr = head

        while curr != None:
            while curr.next != None and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next
    

        return head