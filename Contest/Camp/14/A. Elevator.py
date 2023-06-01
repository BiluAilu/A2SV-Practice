t=int(input())
w=[]
et=[]
ef=[]

for i in range(t):
    x,y,z=map(int,input().split())
    w.append(x)
    et.append(y)
    ef.append(z)

for i in range(t):
    x=w[i]*4
    y=w[i]*ef[i]+(4-ef[i])*et[i]
    z=abs(ef[i]-0)*et[i]+ 4*et[i]
    print(min(x,y,z))