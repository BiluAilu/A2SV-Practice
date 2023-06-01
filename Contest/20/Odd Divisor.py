import math
t=int(input())
n=[]
for i in range(t):
    n.append(int(input()))
# Approch 1
for i in n:
    if i%2==1:
        print("YES")
    else:
        if i==pow(2,int(math.log2(i))):
            print("NO")
        else:
            print("YES")
#Approch 2





# for i in n:
#     if i%2==1:
#         print("YES")
#     else:
#         result=False
#         x=3
#         while(i%2==1):
#             i=i/2
#         while x<=i:
#             if i//x == i/x:
#                 result=True
#                 break
#             x+=2
#         print ("YES" if result else "NO")

