class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:

        '''

        [2,1,4,3]
        [1,2,3,4]
        
        [2,9,2,5,6]
        [2,2,5,6,9]

        [7,3,6,7,1]   left=1  right=4   expected=2


        [2],[2,2][2,2,5][2,2]
        '''
        aL,aR=-1,-1
        # nums.sort()
        ans=0
        for i in range(len(nums)):
            if nums[i]>=left:
                aL=i
            if nums[i]>right:
                aR=i
            ans+=aL-aR
        print(nums[aL],nums[aR])


        return ans
