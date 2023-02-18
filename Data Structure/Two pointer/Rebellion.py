num=int(input())
length=[]
myList=[]
for i in range(num):
    length.append(int(input()))
    myList.append(list(map(int,input().split())))



# print(*myList)
for li in myList:
    l,r=0,len(li)-1
    c=0

    count=li.count(0)
    while l<r:
        if li[l]==1 and li[r]==0:
            
            
            c+=1
            li[l],li[r]=li[r],li[l]
            l+=1
            r-=1
        elif li[l]==0 and li[r]==1:
            l+=1
            r-=1
        elif li[r]==1 and li[r]==1:
            r-=1
        elif li[l]==0 and li[r]==0:
            l+=1
        

    print(c)
               


