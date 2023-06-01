n,d=map(int,input().split())
road=list(input())

curr=0
moves=0
while curr < n:
    if "1" in road[curr+1:curr+d+1]:

        k=curr+1
        while k<n and k<curr+d+1:
            if road[k]=="1":
                index=k
            k+=1

        curr=index
        # print("=======",index)
        if index==n-1:
            print(moves+1)
            exit(0)
            
        moves+=1
    else:
        print(-1)
        exit(0)
print(moves)
