class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ####---------########
        n = len(nums)
        max_or = 0
        max_or_count = 0
        for i in range(1, 1 << n):
            subset_or = 0
            for j in range(n):
                if i & (1 << j):
                    subset_or |= nums[j]
            if subset_or > max_or:
                max_or = subset_or
                max_or_count = 1
            elif subset_or == max_or:
                max_or_count += 1
        return max_or_count

