num=int(input())
length=[]
s=[]

for i in range(num):
    length.append(int(input()))
    s.append(input())
index=0
for i in s:
    l=0
    r=len(i)-1
    while l<r:
        if i[l]!=i[r]:
            length[index]-=2
            l+=1
            r-=1
        else:
            
            break
    index+=1
print(*length,sep="\n")


