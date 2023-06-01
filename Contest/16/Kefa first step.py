# Kefa decided to make some money doing business on the Internet for exactly n days. He knows that on the i-th day (1 ≤ i ≤ n) he makes ai money. Kefa loves progress, that's why he wants to know the length of the maximum non-decreasing subsegment in sequence ai. Let us remind you that the subsegment of the sequence is its continuous fragment. A subsegment of numbers is called non-decreasing if all numbers in it follow in the non-decreasing order.

# Help Kefa cope with this task!

# Input
# The first line contains integer n (1 ≤ n ≤ 105).

# The second line contains n integers a1,  a2,  ...,  an (1 ≤ ai ≤ 109).

# Output
# Print a single integer — the length of the maximum non-decreasing subsegment of sequence a.

n=int(input())
arr=list(map(int,input().split()))

dis=0
l=0
r=0
while r<n:
    l=r
    while r<n-1 and arr[r+1]>=arr[r]:
        r+=1
    dis= max(dis,r-l+1)
    r+=1
print(dis)

# f=0
# m=0
# d=0
# while m<len(arr):
#     d=max(d,m-f+1)
#     if arr[m]>=arr[f]:
#         m+=1
#     else:
#         m+=1
#         f=m
    
# print(d)