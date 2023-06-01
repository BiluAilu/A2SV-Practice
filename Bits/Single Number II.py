class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # dic={}
        # result=0
        # for i in nums:
        #     if i in dic:
        #         dic[i]+=1
        #     else:
        #         dic[i]=1
        # for x in dic:
        #     # print(dic[x])
        #     if dic[x]==1:
        #         return x
        # # return 0

        a = 0
        b = 0 
        for i in nums:
            a = (a ^ i) & ~b
            b = (b ^ i) & ~a
        return a