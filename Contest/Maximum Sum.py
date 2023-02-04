n,m=map(int,input().split())

price=input().split()
for i in range(n):
    price[i]=int(price[i])

price.sort()
sum=0
for i in range(m):
    sum=min(sum,sum+price[i])
    
print( abs(sum))
