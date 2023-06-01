n=int(input())
arr=list(map(int,input().split()))
sorA=sorted(arr)
q=int(input())
newA=[]
for i in range(q):

    newA.clear()
    newA.append(arr)
    typ,left,right=map(int,input().split())
    if typ==1:
        sum=0
        for j in range(left-1,right,1):
            sum+=arr[j]
        print(sum)

    else:
        sum=0
        for j in range(left-1,right,1):
            sum+=sorA[j]
        print(sum)
        