n,m=map(int,input().split())
result=[["." for i in range(m)] for i in range(n)]
dire=1
for i in range(n):
    if i%2==0:

        for j in range(m):
            result[i][j]="#"
    else:
        if dire==1:
            result[i][-1]="#"
            dire=0
        else:
            result[i][0]="#"
            dire=1

for i in range(n):
    for j in range(m):
        print (result[i][j],sep="",end="")
    print()
# print(*result)
        


