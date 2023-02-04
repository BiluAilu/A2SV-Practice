numIn=int(input())
le=[]
num=[]
for i in range(numIn):
    le.append(int(input()))
    num.append( list(map(int,input().split(" "))))
# Solution 1
for i in range(numIn):
    if sum(num[i])==0:
        print("NO")
    else:
        if(sum(num[i])<0):
            num[i].sort()
            print("YES")
            print(*num[i])
        else:
            num[i].sort(reverse=True)
             
            print("YES")
            print(*num[i])


# Solution 2
pos=[]
neg=[]
zero=[]
for i in range(numIn):
    if sum(num[i])==0:
        print("NO")
    else:
        if(sum(num[i])<0):
            num[i].sort()
            print("YES")
            print(*num[i])
        else:
            num[i].sort(reverse=True)
             
            print("YES")
            print(*num[i])

        

# print(num)
