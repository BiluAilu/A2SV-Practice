class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        [1,2,3,4,]

        [1,2,3,4]




        [3,1,3,4,3]
        
        [1,3,3,3,4]
        '''
        
        op=0
        lp,rp=0,len(nums)-1
        nums.sort()
        toBreak=True
        while(lp<rp):
            if(nums[lp]+nums[rp]==k):
                op+=1
                lp+=1
                rp-=1
            elif(nums[lp]+nums[rp]<k):
                lp+=1
            elif(nums[lp]+nums[rp]>k):
                rp-=1
        return op

