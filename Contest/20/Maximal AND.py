t=int(input())
# n,k,array=[],[],[]

for i in range(t):
    ans=0
    n,k=map(int,input().split())
    nums=list(map(int,input().split()))
    for i in range(30,-1,-1):
        count=0
        for num in nums:
            if num& 1<<i==0:
                count+=1
        if count<=k:
            ans+=2**i
            k=k-count
    print(ans)
            
    


