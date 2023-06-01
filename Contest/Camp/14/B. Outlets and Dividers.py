t=int(input())
n=[]
m=[]
a=[]

for i in range(t):
    x,y=map(int,input().split())
    n.append(x)
    m.append(y)
    a.append(list(map(int,input().split())))

for i in range(t):
    if n[i]<=m[i]:
        print(0)
    else:
        a[i].sort(reverse=True)
        c_s=0
        j=0
        counter=0
        while  j<m[i] and c_s <n[i] :
            c_s+=a[i][j]
            counter+=1
            j+=1
        if c_s<n[i]:
            print(-1)
        else:
            print(counter)

