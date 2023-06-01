n1=input()
n2=input()
result=[]
for i in range(len(n1)):
    result.append(int(n1[i])^int(n2[i]))

print(*result,sep="")