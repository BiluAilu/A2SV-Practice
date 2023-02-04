'''

3 7 5 1 10 3 20

1 3 3 5 7 10 20

2 2
3 4

if(k=len(num))
'''

n,k=map(int,input().split(" "))
numbers=input().split()
for i in range(n):
    numbers[i]=int(numbers[i])
numbers.sort()
if  k==0:

    if(numbers[0]==1):
        print(-1)
    else:
        print(numbers[0]-1)
elif(k==len(numbers)):
    if(numbers[-1]==1000000000):
        print(numbers[-1])
    else:
        print(numbers[-1]+1)
else:
    if(numbers[k]!=numbers[k-1]):
        if(numbers[k]-numbers[k-1]>1):
            print(numbers[k-1]+1)
        else:
            print(numbers[k-1])
    else:
        print(-1)
    # print(*numbers)

