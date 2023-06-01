num=int(input())

arrays=[]
for i in range(num):
    arrays.append(list(map(int,input().split())))


for i in range(num):
    x=(arrays[i][0]+arrays[i][1])//4

    if x> min(arrays[i][0],arrays[i][1]):
        print(min(arrays[i][0],arrays[i][1]))
    else:
        print(x)