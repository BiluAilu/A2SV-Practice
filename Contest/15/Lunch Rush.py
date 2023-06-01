n,k=map(int,input().split())
time=[]
fun=[]
for i in range(n):
    x,y=map(int,input().split())
    fun.append(x)
    time.append(y)
result=-55555555555
for i in range(n):
    if time[i]>k:
        result=max(result,(fun[i]-(time[i]-k)))
    else:
        result=max(result,fun[i])
print (result)
