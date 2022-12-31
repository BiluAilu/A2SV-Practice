
num=int(input())
op=[]
number_of_operation=int(input())
for i in range(number_of_operation):
    op.append(str(input()))

for i in op:
    if(i=="++X"):
        num+=1
    elif(i=="X++"):
        num+=1
    elif(i=="X--"):
        num-=1
    elif(i=="--X"):
        num-=1
    else:
        print("Error input")
        break
print(num)