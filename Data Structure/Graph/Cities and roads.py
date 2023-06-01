n=int(input())

matrix=[]

for i in range(n):
    a=list(map(int,input().split()))
    matrix.append(a)

result=0
for i in range(n):
    for j in range(i,n):
        if matrix[i][j]==1:
            result+=1

print(result)
