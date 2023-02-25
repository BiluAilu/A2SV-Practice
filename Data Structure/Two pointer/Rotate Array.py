class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''
        [1,2,3,4,5,6,7]  k=3
        .........----->
                *
                


        
        '''
        b=(len(nums)-k)%len(nums)
        nums[:]=nums[b:]+nums[:b]