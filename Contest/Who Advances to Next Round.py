
n,k= map(int, input().split())
inp=input().split()
ch=int(inp[k])

count=0
if ch==0:
    print(0)
else:
    for i in range(len(inp)):
        if int(inp[i])>=ch:
            count+=1
        else:
            break
    print(count)