n,k=map(int,input().split(" "))
numbers=input().split()
for i in range(n):
    numbers[i]=int(numbers[i])
numbers.sort()

if(numbers[k]!=numbers[k-1]):
    if(numbers[k]-numbers[k-1]>1):
        print(numbers[k-1]+1)
    else:
        print(numbers[k-1])
else:
    print(-1)
# print(*numbers)

