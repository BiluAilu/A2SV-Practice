num=int(input())
li=[]
result=200001
for i in range(num):
    li.append(input())
# print(*li)
for i in range(len(li)):
    wind=0
    l=0
    p=0
    s=set()
    found=False
    for j in range(len(li[i])):
        if li[i][j] == li[i][l]:
            print("I am here")
            l+=1
            while l>0 and li[i][l]!=li[i][l+1]:
                l+=1
        p+=1
        s.add(li[i][j])
        result=min(result,p-l+1)
        print(s)
        
        if len(s)==3:
            found=True
            break

    if found:
        print(result)
    else:
        print(0)
