            
class Solution:
    def insertionSortList(self, head):
        current = head
        while current:
            temp = head
            while temp != current:
                if  temp.val > current.val: 
#swap values
                    temp.val, current.val = current.val,  temp.val
                temp =  temp.next
            current = current.next
        return head            
            


