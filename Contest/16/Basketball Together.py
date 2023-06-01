import math

n,p=map(int,input().split())
team=list(map(int,input().split()))
team.sort()
win=0
l=0
r=len(team)-1

while l<=r:
    needNumber=math.ceil(p/team[r])
    if p%team[r]==0:
        needNumber+=1

    if (r-l+1)>=needNumber:
        l+=needNumber-1
        r-=1
        win += 1
    else:
        break
print(win)
