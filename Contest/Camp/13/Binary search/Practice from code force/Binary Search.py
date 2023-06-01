n,k=map(int,input().split())
arr=list(map(int,input().split()))
query=list(map(int,input().split()))

for i in range(k):
    t=query[i]
    l=0
    r=n-1
    found=False
    while l<=r:
        mid=(l+r)//2
        if arr[mid]<t:
            l=mid+1
        elif arr[mid]>t:
            r=mid-1
        else:
            print("YES")
            found=True
            break
    if not found:
        print("NO")

