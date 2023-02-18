from math import inf
n,s=map(int,input().split())
a=list(map(int,input().split()))

min_l=inf
right=0
current_sum=0

for left in range(len(a)):
    while right<n and (current_sum<s):
        current_sum+=a[right]
        right+=1
    if current_sum>=s:
        min_l=min(min_l,right-left)
    else:
        break
    current_sum-=a[left]
print(min_l if min_l !=inf else -1)