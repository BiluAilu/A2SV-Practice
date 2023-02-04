class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        '''
        [3,5,2,3]
        [2 3 3 5]

        [3 5 4 2 4 6]
        [2 3 4 4 5 6]
        
        '''
        nums.sort()
        sum=0
        lp,rp=0,len(nums)-1
        while(lp<rp):
            sum=max(sum,nums[lp]+nums[rp])
            lp+=1
            rp-=1
        return sum