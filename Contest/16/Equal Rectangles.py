n=int(input())
q=[]
sides=[]
# Parea=-1
for i in range(n):
    q.append(int(input()))
    sides.append(list(map(int,input().split())))

for i in range(n):
    result =True
    sides[i].sort()
    if sides[i][0]!= sides[i][1] or  sides[i][-1]!= sides[i][-2]:
        print("NO")
        continue
    area=sides[i][0]*sides[i][-1]
    l=2
    r=len(sides[i])-3
    while l<r:
        if sides[i][l]!= sides[i][l+1] or  sides[i][r]!= sides[i][r-1]:
            print("NO")
            result=False
            break
        if sides[i][l]*sides[i][r]!=area:

            print("NO")
            result=False
            break
        l+=2
        r-=2
    if result:
        print("YES")
# for i in range(n):
#     b=True
#     sides[i].sort()
#     l=0
#     r=len(sides[i])-1
#     while l<r:
#         if sides[i][l]*sides[i][r]==sides[i][l+1]*sides[i][r-1]:
#             if l:
#                 if sides[i][l-2]*sides[i][r+2]!=sides[i][l]*sides[i][r]:
#                     b=False
#                     break
                 
            
#             l+=2
#             r-=2
#         else:
#             b=False
#             break
#     if b:
#         print("YES")
#     else:
#         print("NO")
