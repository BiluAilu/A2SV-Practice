num=int(input())
nums=list(map(int,input().split()))

numQ=int(input())
questions=[]
for i in range(numQ):
    questions.append(list(map(int,input().split())))
print('I am here')
pr_sum=[0]*num
pr_sum[0]=nums[0]
for i in range(1,len(nums)):
    pr_sum[i]=nums[i]+pr_sum[i-1]

nums.sort()
sor_pr_sum=[0]*num
sor_pr_sum[0]=nums[0]
for i in range(1,len(nums)):
    sor_pr_sum[i]=nums[i]+sor_pr_sum[i-1]

print(sor_pr_sum)
print(pr_sum)
for i in range(numQ):
    if questions[i][0]==1:
        print(pr_sum[questions[i][2]+1] - pr_sum[questions[i][1]])
    else:
        print(sor_pr_sum[questions[i][2]+1] - sor_pr_sum[questions[i][1]])
