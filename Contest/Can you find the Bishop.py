numIn=int(input())
board=[]

for i in range(numIn):
    b=[]
    for j in range(8):
        b.append(input())
    board.append(b)
# print(board[0])
for i in range(len(board)):
    for j in range(1,7):
        if board[i][j].count("#")==1:
            index=board[i][j].index("#")
            print(index+1)
            print(f'{i+1} {j+1}')
            break

