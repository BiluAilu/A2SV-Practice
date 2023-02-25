n=int(input())
boys=list(map(int,input().split(" ")))

m=int(input())
girls=list(map(int,input().split(" ")))

girls.sort()
boys.sort()

te=0
t,l,s=0,0,0

while t<len(boys):
    while s<len(girls) :
        if( boys[t]==girls[s]+1 or boys[t]==girls[s]-1 ):
            l+=1
            s=l
            te+=1
            break
        else:
            s+=1
    t+=1
    s=l
print(te)