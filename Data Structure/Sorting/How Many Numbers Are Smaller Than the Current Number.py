class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # out=[0]*len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i]>nums[j]:
        #             out[i]+=1
        # print(out)
        # return out
        '''
        8,1,2,2,3

        1,2,2,3,8
        '''
        out=[]
        num=sorted(nums)
        indexes={}
        for i in range(len(num)):
            if num[i] not in indexes:
                indexes[num[i]]=i
        for i in nums:
            out.append(indexes[i]) 
        print(out)
        return out




