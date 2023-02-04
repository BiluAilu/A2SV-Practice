n=int(input())

seg=[]
x=[]
y=[]
for i in range(n):
    seg.append(list(map(int,input().split())))
    x.append(seg[i][0])
    y.append(seg[i][1])

minX=min(x)
maxY=max(y)

try :
    
    print(seg.index([minX,maxY])+1)
    
except:
    print(-1)
