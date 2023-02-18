n,s=map(int,input().split())
a=list(map(int,input().split()))

max_l=0
right=0
current_sum=0

for left in range(len(a)):
    while right<n and (current_sum +a[right]<=s):
        current_sum+=a[right]
        right+=1
    max_l=max(max_l,right-left)
    current_sum-=a[left]
print(max_l)