

# t=int(input())
# grid=[]
# directions = [(0,1),(1,0),(-1,0),(0,-1)]
# for i in range(t):
#     grid=[]
#     row,col=map(int,input().split())
#     for j in range(row):
#         grid.append(list(map(int,input().split())))
#     visited=[[0 for i in range(col)] for j in range(row)]
#     def inbound(row, col):            
#           return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
#     def dfs(row,col):
#             visited[row][col]=True
#             depth=grid[row][col]


#             for r,c in directions:
#                 new_row=row+r
#                 new_col=col+c
#                 if inbound(new_row,new_col) and visited[new_row][new_col]==False and grid[new_row][new_col]>0:
#                     depth+=dfs(new_row,new_col)
#             return depth
#     result=0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j]>0 and visited[i][j]==False:
#                 result=max(result,dfs(i,j))
#     print (result)


    
t = int(input())
grid = []
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for _ in range(t):
    grid = []
    row, col = map(int, input().split())

    for _ in range(row):
        grid.append(list(map(int, input().split())))

    visited = [[False for _ in range(col)] for _ in range(row)]

    def inbound(row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    result = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 0 and not visited[i][j]:
                stack = [(i, j)]
                depth = 0

                while stack:
                    curr_row, curr_col = stack.pop()
                    if not visited[curr_row][curr_col]:
                        visited[curr_row][curr_col] = True
                        depth += grid[curr_row][curr_col]

                        for r, c in directions:
                            new_row = curr_row + r
                            new_col = curr_col + c

                            if inbound(new_row, new_col) and not visited[new_row][new_col] and grid[new_row][new_col] > 0:
                                stack.append((new_row, new_col))

                result = max(result, depth)

    print(result)

    