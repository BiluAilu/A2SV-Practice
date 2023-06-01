num =int(input())
 
l=1
r=num
 
while l<r:
    print(l,end=" ")
    print(r,end=" ")
    l+=1
    r-=1
if num%2==1:
    print(l)