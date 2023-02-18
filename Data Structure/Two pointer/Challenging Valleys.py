num=int(input())
for i in range(num):
    s=int(input())
    nums=[int(i) for i in input().split()]
    z=0
    for l in range(s-1):
        if nums[l]<nums[l+1]:
            break
        z+=1
    for r in range(z,s-1):
        if nums[r]>nums[r+1]:
            print("NO")
            break
        z+=1
    if z==s-1:
        print("YES")