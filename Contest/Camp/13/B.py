num=int(input())
length=[]
arrays=[]

for i in range(num):
    length.append(int(input()))
    arrays.append(list(map(int,input().split())))

for i in range(num):
    arrays[i].sort()


for k in range(num):
    if length[k]==1:
        print("YES")
        continue
    c=True
    i=0
    j=1
    while j<length[k]:
        if arrays[k][i]-arrays[k][j]==1 or arrays[k][i]-arrays[k][j]==-1 or arrays[k][i]-arrays[k][j]==0:
            j+=1
            i+=1
        else:
            print("NO")
            c=False
            break
    if c:
        print("YES")
