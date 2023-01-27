class Solution:
    def shiftZeros(self,nums:List[int]):
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]  # Partitioning the array
                j += 1
        
    def applyOperations(self, nums: List[int]) -> List[int]:
        if(len(nums)>=2):
            for i in range(len(nums)-1):
                if(nums[i]==nums[i+1]):
                    nums[i]=nums[i]*2
                    nums[i+1]=0
        
        
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j] 
                j += 1
        return nums
    