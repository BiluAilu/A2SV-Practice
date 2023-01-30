power,num=map(int,input().split())
# print(power)
bonus=[]
dragonP=[]
for i in range(num):
    x,y=map(int,input().split())
    dragonP.append(x)
    bonus.append(y)
# print(*bonus)
win=True
for i in range(num):
    if(power>dragonP[i]):
        power+=bonus[i]
    else:
        win=False
        break
if(win):
    print("YES")
else:
    print("NO")

