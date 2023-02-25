pages=list(map(int,input().split(",")))

pages.sort()
result=[[pages[0]]]
k=0
for i in range(1,len(pages)):
    if pages[i]-pages[i-1]==0 or pages[i]-pages[i-1]==1:
        result[k].append(pages[i])


    else:
        k+=1
        result.append([pages[i]])

for i in range(len(result)):
    if result[i][0]-result[i][-1]==0:
        print(result[i][0],end="",sep="")
    else:
        print(result[i][0],"-",result[i][-1],end="",sep="")
    if i!=len(result)-1:
        print(',',end="",sep="")
# print(*pages)