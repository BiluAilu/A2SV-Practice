# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr=[]
        result=[]

        if head==None and head.next==None:
            return head
        while head:
            arr.append(head.val)
            head=head.next
        
        left-=1
        right-=1
        # print(*arr)
        arr[left:right + 1] = arr[left:right + 1][::-1]
        print(*arr)
        for i in range(0,len(arr)):
            arr[i] = ListNode(arr[i])
        for i in range(0,len(arr)-1):
            arr[i].next=arr[i+1]
            print(arr[i].val)
        return arr[0]
