num=int(input())
length=[]
black=[]
strip=[]
for i in range(num):
    x,y=map(int,input().split(" "))
    length.append(x)
    black.append(y)
    strip.append(input())


for s in strip:
    if len(s)==1 and s[0]=='W':
        print(1)
        break
    elif len(s)==1 and s[0]=='B':
        print(0)
        break

    indexes=[]
    for i in range(len(s)):
        if s[i]=='B':
            indexes.append(i)
    
    



