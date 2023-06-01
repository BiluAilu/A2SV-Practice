# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        G=ListNode()
        L=ListNode()
        temp=head
        GH=G
        LH=L
        while temp:
            if temp.val >= x:
                print('Greater')
                GH.next=temp
                temp=temp.next
                GH=GH.next
                GH.next=None
                

                
            else:
                print("Less")
                LH.next=temp                
                temp=temp.next
                LH=LH.next
                LH.next=None
            print(G)
            print(L)
            # temp=temp.next
        LH.next=G.next
        return L.next


  