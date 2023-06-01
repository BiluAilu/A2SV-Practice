class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        l,r=0,len(people)-1

        '''
        [3,2,2,1]=>[1,2,2,3]    l=3


        
        '''
        
        while l<r:
            if people[l]+people[r]>limit:
                count+=1
                r-=1
            else:
                count+=1
                r-=1
                l+=1
        if l==r:
            count+=1
        return count