n,t=map(int,input().split())
a=list(map(int,input().split()))

visited=set()
visited.add(1)

i=1

while i <n:
    i+=a[i-1]
    visited.add(i)
if t in visited:
    print("YES")
else:
    print("NO")










# n,t=map(int,input().split())
# a=list(map(int,input().split()))
# found=False
# i=1
# while i<n:
#     if i==t:
#         print("YES")
#         found=True
#         break
#     else:
#         if i+a[i-1]==i:
#             print("YES")
#             found=True
#             break

#     i=a[i-1]+i
# if not found:
#     print("NO")
