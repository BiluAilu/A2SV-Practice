n=int(input())
nums=[]
win=0
for i in range(n):
    nums.append(list(map(int,input().split())))
# print(nums)

for i in range(len(nums[0])):
    rowSum=sum(nums[i])
    for j in range(len(nums[0])):
        colSum=0
        for k in range(len(nums[0])):
            colSum+=nums[k][j]
        if colSum>rowSum:
            win+=1
print(win)


