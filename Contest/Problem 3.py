num=int(input())

coin=input()
coins=[]
con=coin.split(" ")
for i in range(len(con)):
    coins.append(int(con[i]))

sumT=sum(coins)
mysumI=0
mysum=0
myLen=0
herLen=len(coins)
while(myLen<herLen):
    mysum=max(coins)+mysum
    j=coins.index(max(coins))
    sumT=sumT-max(coins)
    mysumI+=1
    coins.pop(j)
    
    if(mysum>sumT):
        break
print(mysumI)

