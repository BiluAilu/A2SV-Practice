n,m=map(int,input().split())
names=[]
negative=[]
for i in range(n):
    names.append(input())
for i in range(m):
    negative.append(input().split())

if m==0:
    names.sort()
    print(n)
    print(*names,sep="\n")
else:
    