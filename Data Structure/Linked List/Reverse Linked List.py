# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        current_element_toBe_processed=head
        head=None

        while current_element_toBe_processed!=None:
            nxt=current_element_toBe_processed.next #for later use
            #head is the new node to inserted into the reversed linked list
            current_element_toBe_processed.next=head
            head=current_element_toBe_processed
            current_element_toBe_processed=nxt
        return head

