n,m=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort(reverse=True)
# print(a)
for i in range(len(b)):
    j=0
    while b[i]<a[j] and j<len(a)-1:
        j+=1
            
    print(len(a)-j,end=" ")
            
