n=int(input())
reposts=[]

for i in range(n):
    reposts.append(list(input().split()))

checked=False
lastRepost=""
repost=0
for i in range(n):
    if (reposts[i][-1]).lower() =="polycarp" and not checked:
        lastRepost=reposts[i][0]
        repost+=2
        checked = True
    elif (reposts[i][-1]).lower() !="polycarp" and (reposts[i][-1]).lower() == (reposts[i-1][0]).lower():

        repost+=1
        lastRepost=reposts[i][0]
    elif (reposts[i][-1]).lower() !="polycarp" and (reposts[i][-1]).lower()==lastRepost:
        repost+=1


print(repost)