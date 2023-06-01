
def main():

    num=list(map(int,input()))
    # print(num)
    valid=[1,14,144]
    invalid=[0,2,3,5,6,7,8,9]

    for i in invalid:
        if i in num:
            print("NO")
            return
    
    ind=0
    c=1
    p=num[ind]
    if p not in valid:
        print("NO")
        return
    while ind<len(num) and c<len(num):

        
        if p*10+num[c] in valid:
            p=p*10+num[c]
            c+=1
        
        else:
            ind=c
            c=ind+1
            if num:
                p=num[ind]
                if p not in valid:
                    print("NO")
                    return
    print("YES")






##OTHER SOLUTIONS
# i, s = 0, input()
# ok = True

# while i<len(s):
    
#         if s[i:i+3]=='144':
#             i+=3
#         elif s[i:i+2]=='14':
#             i+=2
#         elif s[i]=='1':
#             i+=1
#         else:
#             ok=False
#             break

# if ok:
#     print('YES')
# else:
#     print('NO')










main()
