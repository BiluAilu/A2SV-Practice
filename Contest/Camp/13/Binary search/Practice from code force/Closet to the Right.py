n,k=map(int,input().split())
arr=list(map(int,input().split()))
query=list(map(int,input().split()))

for i in range(k):
    l=-1
    r=n
    while  (l+1<r):
        mid=(l+r)//2
        if arr[mid]<=query[i]:
            l=mid
        elif arr[mid]>query[i]:
            r=mid

    if l==-1:
        print(1)
    elif r==n:
        print(r)
    else:
        print(r+1)
    

