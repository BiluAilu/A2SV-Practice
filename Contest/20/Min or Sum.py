t=int(input())
length=[]
a=[]
for i in range(t):
    length.append(int(input()))
    a.append(list(map(int,input().split())))

for i in range(t):
    result=0
    for i in a[i]:
        result|=i
    print(result)