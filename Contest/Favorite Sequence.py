num=int(input())
length=[]
lists=[]
for i in range(num):
    length.append(int(input()))
    lists.append(list(map(int,input().split())))

result=[]
for li in lists:
    l,r=0,len(li)-1
    i=0
    re=[0]*len(li)
    while l<=r:
        if i%2==0:
            re[i]=li[l]
            l+=1
            
        else:
            re[i]=li[r]
            r-=1
            
        i+=1
    result.append(re)


for l in result:
    print(*l)
