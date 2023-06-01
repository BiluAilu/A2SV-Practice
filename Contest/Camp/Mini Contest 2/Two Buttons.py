n,m = map(int, input().split())
op = 0
while n != m:
    
    if m%2==0 and m>n:
        m=m/2
    else:
        m=m+1
 
    op += 1
print(op)