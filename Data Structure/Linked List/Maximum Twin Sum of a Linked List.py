# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp=head
        temp2=head
        length=0
        sum=0
        while temp:
            temp=temp.next
            length+=1
        '''
        5,4,2,1
        '''
        for i in range((length//2)-1):
            temp2=temp2.next
        
        t3=temp2
        temp2=temp2.next
        print(temp2)
        print(prev)

        t3.next=None
        #
        '''
        5->4->2   2->4->5->none
        '''
        if head or head.next:
            cur=head
            temp=cur.next
            prev=None
            

            while temp:
                cur.next=prev
                prev=cur
                cur=temp
                temp=temp.next

        print(temp2)
        print(prev)
        
        while temp2 and prev:
            sum=max(sum,temp2.val+prev.val)
            prev=prev.next
            temp2=temp2.next
        
        return sum





