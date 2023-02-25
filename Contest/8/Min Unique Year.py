num=int(input())

s=set()
num+=1

while True:
    for i in range(len(str(num))):
        s.add(str(num)[i])
    if(len(s)==len(str(num))):
        break
    else:
        num+=1
        s.clear()

print(num)

