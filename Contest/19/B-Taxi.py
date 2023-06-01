# n=int(input())
# groups=list(map(int,input().split()))

# # groups.sort(reverse=True)
# full_groups=0
# three_member_groups=0
# two_member_groups=0
# one_member_groups=0
# while groups:
#     if groups[-1]==4:
#         groups.pop()
#         full_groups+=1
#     elif groups[-1]==3:
#         if one_member_groups:
#             one_member_groups-=1
#             full_groups+=1
#         else:
#             three_member_groups+=1
#         groups.pop()
#     elif groups[-1]==2:
#         if two_member_groups:
#             two_member_groups-=1
#             full_groups+=1
#         else:
#             two_member_groups+=1
#         groups.pop()
#     elif groups[-1]==1:
#         if three_member_groups:
#             three_member_groups-=1
#             full_groups+=1
#         else:
#             one_member_groups+=1
#         groups.pop()
#     if one_member_groups>0:
#         if one_member_groups%2==0:
#             two_member_groups+=1
#             one_member_groups=0
#     if two_member_groups==2:
#         full_groups+=1
#         two_member_groups=0
# temp_group=0
# if two_member_groups==1 and one_member_groups==1:
#     temp_group+=1
#     two_member_groups=0
#     one_member_groups=0

# # print(temp_group)   
# # print(full_groups,three_member_groups,two_member_groups,one_member_groups)
# print(full_groups+three_member_groups+two_member_groups+one_member_groups+temp_group)


import math

n=int(input())
groups=list(map(int,input().split()))

four=groups.count(4)
three=groups.count(3)
two=groups.count(2)
one=groups.count(1)

x=max(0,one-three)
two_to_four=two//2
two=two%2

ans=four+three+two_to_four+((two*2+x+3)//4)
print(ans)