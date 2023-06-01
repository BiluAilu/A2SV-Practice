import sys
n=int(input())

inp=[]
for i in range(n):
    x=sys.stdin.readline().strip()
    inp.append(int(x))
inp.sort()

l=0
r=(n+1)//2
pair=0



while r<n:
    while r < n and inp[l]*2 > inp[r]:
        r+=1
    if r < n  :
        pair+=1
    l+=1
    r+=1
print(n-pair)
