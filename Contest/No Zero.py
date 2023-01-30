numIn=int(input())
le=[]
num=[]
for i in range(numIn):
    le.append(int(input()))
    num.append( list(map(int,input().split(" "))))
for i in range(numIn):
    if sum(num[i]==0):
        print("NO")
    else:
        

print(num)
