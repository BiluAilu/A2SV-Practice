class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        indices=[]
        for index,value in enumerate(nums):
            if value==target:
                indices.append(index)
        print(indices)
        return indices