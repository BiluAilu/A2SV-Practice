def hasSameSign(a: int, b: int) -> bool:
    return (a >= 0 and b >= 0) or (a < 0 and b < 0)

n=int(input())
l=[]
a=[]
sum=0
for i in range(n):
    l.append(int(input()))
    a.append(list(map(int,input().split())))
# print(l)
for i in range(n):
    sum=0
    flag=0
    m=a[i][0]
    left=0
    right=l[i]
    # print("\n--------------------New-----------------------------")
    # print(a[i])
    for left in range(len(a[i])):

        # if abs(a[i][flag])+abs(a[i][left])==abs(a[i][left]+a[i][flag]):
        if hasSameSign(a[i][flag],a[i][left]):
            m=max(m,a[i][left])
            left+=1
        else:
            # print("Different sign")
            # print(m)
            sum=sum+m
            # print(sum)
            m=a[i][left]
            # print(m)
            flag=left
            

    # print("**********************************************\n\n")
        
    sum=sum+m  
    # print(a[i])
    print(sum)


