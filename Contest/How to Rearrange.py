# num=int(input())
# s=[]
# for i in range(num):
#     s.append(input())

# for i in s:
#     if i[::-1]!=i:
#         print(i)
#     else:
#         print("How?")
       
            
#         l=len(i)
#         i[int(l/2)],i[int(l/2)+1]=i[int(l/2)+1],i[int(l/2)]
#         if i[::-1]!=i:
#             print(i)
#         else:
#             print(-1)
#             break
#         # c=set()
            
        
        
for _ in range(int(input())):
    s=sorted(input())

    if s[0]==s[-1]:
        print(-1)
    else:
        print(''.join(s))