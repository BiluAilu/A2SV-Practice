
# def check(l:int,c:str,s:str):
#     pos=[i for i,v in enumerate(s) if v==c]
    
#     #print(pos)
#     count=1
#     for j in pos:
#         #print(j)
#         if(j+1==len(s)):
#             j=-1
#         if(s[j+1]=="g"):
#             distance.append(count)
#             #print("I am here")
#             count=1
#             continue
#         else:
#             count+=1
#                 # print(count)
    
#     return max(distance)
    
    
# num=int(input())
# # length_and_char
# length=[]
# chars=[]
# strings=[]
# distance=[]
# for i in range(num):
#   length_and_char=input()
#   length.append(int(length_and_char.split(" ")[0]))
#   chars.append((length_and_char.split(" ")[1]))
#   strings.append(input())
# # print(length)
# # print(chars)
# # print(strings)
# # print(length)
# for j in range(num):
#     if(len(strings[j])==0):
#         #print("I am here")
#         print ("0")
#     else:
        
#         print(check(length[j],chars[j],strings[j]))




def Check_distance(s:str,l:int,c:str): 
    
    if c=='g':
        print("0")
        return
    cidx=[]
    gidx=[]

    for i in range(len(s)):
        if i<l and s[i]==c:
            cidx.append(i)
        elif s[i]=='g':
            gidx.append(i)
    result=0
    i=0

    for j in range(len(cidx)):
        while cidx[j]>gidx[i]:
            i+=1
        result=max(result,gidx[i]-cidx[j])
    print(result)


num_of_input=int(input())
for i in range(num_of_input):
    S_length,character=input().split()
    S_length=int(S_length)
    S_value=input()*2
    Check_distance(S_value,S_length,character)




