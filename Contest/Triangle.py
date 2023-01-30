num=int(input())
s=input().split(" ")
arr=[]
can=False
for i in range(num):
    arr.append(int(s[i]))
# print(arr)
if num<3:
    can=False
else:
    arr.sort()
    for i in range(num-2):
        if arr[i]+arr[i+1]>arr[i+2]:
            can=True
            break
if can:
    print("YES")
else:
    print("NO")