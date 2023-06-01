num=int(input())
t=list(map(int,input().split()))

t.sort()
wait=0
happy=0
for i in range(num):
    if num[i]<wait:
        happy+=1
    wait+=num[i]

print(happy)   



