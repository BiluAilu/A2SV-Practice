num=int(input())
p=[]
for i in range(num):
    p.append(input().split(" "))

# print(p)
sum=[]
for i in range(len(p[0])):
    sum_=0
    for j in range(num):
        # print(p[j][i])
        sum_=sum_+int(p[j][i])
    sum.append(sum_)
if(sum[0]==0 and max(sum)==0 and min(sum)==0):
    print("YES")
else:
    print("NO")



