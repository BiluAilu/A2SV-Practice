import math
num=int(input())
rows=[]
for i in range(num):
    rows.append(input().split())
    rows.append(input().split())

for i in range(0,num*2, 2):
    
    area=(int(rows[i][0])*int(rows[i][1]))+(int(rows[i+1][0])*int(rows[i+1][1]))

    if (math.sqrt(area)==round(math.sqrt(area),1)):
        print("YES")
    else:
        print("NO")