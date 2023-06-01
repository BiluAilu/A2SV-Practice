# from collections import deque
# directions=[(1,0),(0,1),(1,1),(-1,1),(0,-1),(-1,0)]

# t=int(input())
# for i in range(t):
#     found=False
#     level=[]
#     n=int(input())
#     level.append(list(input()))
#     level.append(list(input()))
#     visited=[[0 for i in range(n)] for i in range(2)]
#     queue=deque()
#     queue.append((0,0))
#     visited[0][0]=1

#     while queue:
    
#         i,j=queue.popleft()
#         if i==1 and j==n-1:

#             print("YES")
#             found=True
#             break
            

            
        
#         for r,c in directions:
#             new_row=i+r
#             new_col=j+c
#             if 0<=new_row<2 and 0<=new_col<n and visited[new_row][new_col]==0 and level[new_row][new_col]=="0":
#                 visited[r][c]=1
#                 queue.append((new_row,new_col))
#     if not found:
#         print("NO")




t=int(input())
level=[]
for i in range(t):
    level.clear()
    noPath=False
    n=int(input())
    level.append(list(input()))
    level.append(list(input()))
    for j in range(n):
        if level[0][j]=="1" and level[1][j]=="1":
            print("NO")
            noPath=True
            
            break
    if not noPath:
        print("YES")
    
