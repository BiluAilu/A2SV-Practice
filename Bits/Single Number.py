class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        val=0
        for i in nums:
            val^=i
        # print(val)
        return val