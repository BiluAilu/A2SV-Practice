n=int(input())
degree=[]
for i in range(n):
    degree.append(int(input()))

degree.sort()
traveled=set()
if sum(degree)%360==0:
    print("YES")
else:
    prev=0
    l=0
    r=len(degree)-1
    while l<r:
        if degree[l]+prev==degree[r]:
            prev=0
            traveled.add(r)
            traveled.add(l)
            r-=1
            l+=1
        else:
            prev+=degree[l]
            traveled.add(l)
            l+=1

    if l in traveled and prev==0:
        print("YES")


    # if prev==0:
    #     print("YES")
    else:
        print("NO")
