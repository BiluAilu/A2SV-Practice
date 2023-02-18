nums=int(input())
cards=list(map(int,input().split()))

serSum=0
DimSum=0
l,r=0,nums-1
turn=0
while l<=r:
    if cards[l]>cards[r]:
        if turn==0:
            serSum+=cards[l]
            turn=1
        else:
            DimSum+=cards[l]
            turn=0
        l+=1
    else:
        if turn==0:
            serSum+=cards[r]
            
            turn=1
        else:
            DimSum+=cards[r]
            
            turn=0
        r-=1

print(serSum,DimSum)