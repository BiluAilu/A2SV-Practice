n=int(input())
a=list(map(int,input().split()))
li=list(input())

for i in range(len(a)):
    if li[i]=="1":
        for j in range(i+1,len(a)):
            if j<len(a) and li[j]=="1" and a[j]<a[i]:
                a[j],a[i] = a[i],a[j]

if a.isSorted():
    print("YES")
else:
    print("NO")

