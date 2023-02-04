# Time Limit Exceeded 😒
# class Solution:


#     def maxFrequency(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         r=len(nums)-1
#         l=0
#         ra=1
#         while(r>=0):
#             l=0
#             while(l<r):
                
#                 if(nums[r]*(r-l)<= sum(nums[l:r])+k):
#                     ra=max(ra,r-l+1)
#                 l+=1
#             r-=1
        
#         return ra
                

            

#         '''
#     l        r
#     [1,5,5,5,6]  k=3
#     1 2  3 4 5
#     0 1  2  3 4

#         l  r
#         1,4,8,13   req=4  av=1+5

# out=2

#         dif[1][]

#         dif.append(nums[i+1]-nums[i])

#         3,4,5




#         '''

        
 #  The correct version
 class Solution:
    def maxFrequency(self, nums, k: int) -> int:
        ans=0
        total_sum=0
        l=r=0
        nums.sort()
        while r<len(nums):
            total_sum+=nums[r]
            if (r-l+1)*nums[r] >total_sum+k:
                total_sum-=nums[l]
                if ans<r-l:
                    ans=r-l
                l+=1
            r+=1
        if ans<r-l:
            ans=r-l
        return ans       
