import sys
from collections import defaultdict

n=int(input())
graph=defaultdict(list)

for i in range(1,n+1):
    line=list(map(int,input().split()))
    for j in range(len(line)):
        if line[j]==1:
            graph[i].append(j+1)

source=[]
sink=[]
for g in graph:
    source.append(g)
    for l in graph[g]:
        sink.append(l)
for i in range(1,n+1):
    if i  not in source and i not in sink:
        source.append(i)
        sink.append(i)
print(*source)
print(*sink)

# source.sort()
# sink.sort()




#             # val=1
#             # break

# # print(*graph[1])

# for g in graph:
#     if len(graph[g]):
#         source.append(g)
#     else:
#         sink.append(g)

# # for i in range(len(graph)):
# #     if len(graph[i])==0:
# #         sink.append(graph[i])
# #     else:
# #         source.append(graph[i])
# print (*source)
# print(*sink)



# #     if val:
# #         sink.append(i+1)
# #     else:
# #         source.append(i+1)
# # print(*source)
# # print(*sink)
    