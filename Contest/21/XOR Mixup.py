t=int(input())

for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        x=0
        for j in range(n):
            if j!=i:
                # print()
                x= x ^ a[j]
            

        if x==a[i]:
            print(a[i])
            break
