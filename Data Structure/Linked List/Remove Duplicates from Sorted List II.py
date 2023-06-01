# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head==None:
            return head
        if head.next==None:
            return head
        elif head.next.next==None:
            if head.val==head.next.val:
                return None
            else:
                return head
        # elif head.next.next:
        else:
            p=head
            c=head.next
            n=head.next.next
            while n:
                if  p.val==c.val and c.val==n.val:
                    while n and n.val==c.val:
                        n=n.next
                    if n:
                        p=n
                        head=p
                        c=n.next
                        if n.next:
                            n=n.next.next
                        else:
                            n=None
                    else:
                        return None
                elif p.val==c.val:
                    p=n
                    c=n.next
                    head=p
                    if n.next:
                        n=n.next.next
                    else:
                        n=None
                    
                elif c.val==n.val:
                    while n and n.val==c.val:
                        n=n.next
                    if n:
                        p.next=n
                        c=n
                        n=n.next
                    else:
                        p.next=None


                else:
                    p=c
                    c=n
                    n=n.next
            if p and c and not n:
                if p.val==c.val:
                    
                    p=None
                    head=p
                
        
        # pr=head
        # cur=head.next

        # while cur:
        #     if cur.val==pr.val:
        #         temp=cur
        #         cur=cur.next.next
        #         pr.next=cur
        #     else:
        #         pre=cur
        #         cur=cur.next
        return head
                
