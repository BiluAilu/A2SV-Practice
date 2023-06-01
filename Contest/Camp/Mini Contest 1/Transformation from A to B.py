given,target=map(int,input().split())

atSomePointT=target
while True:
    if atSomePointT%2==1:
        break
    atSomePointT//=2
atSomePointG=given
found=False
while atSomePointG<atSomePointT:
    if atSomePointG*10+1==atSomePointT:
        found=True
        break
    else:
        atSomePointG*=2

result=[]
if found:
    print("YES")
    while given<atSomePointG:
        result.append(given)
        given*=2
    result.append(atSomePointG)
    while atSomePointT<=target:
        result.append(atSomePointT)
        atSomePointT*=2
    print(len(result))
    print(*result)
else:
    print("NO")
