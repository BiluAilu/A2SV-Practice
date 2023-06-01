n=int(input())
s=list(input())
result=0

for i in range(n):
    if s[i]=='-':
        if result:
            result-=1
    else:
        result+=1
print(result)
