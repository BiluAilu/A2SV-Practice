n=int(input())
num=list(map(int,input().split()))

num.sort()

for i in range(len(num)):
    if i%2==0 and i>0:
        if num[i]>num[i-1]:
            num[i],num[i-1]=num[i-1],num[i]
    else:
        if num[i]<num[i-1]:
            num[i],num[i-1]=num[i-1],num[i]
print(*num)
