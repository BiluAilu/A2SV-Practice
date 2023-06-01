import sys
from collections import defaultdict

n=int(input())
graph=defaultdict(list)

for i in range(1,n+1):
    line=list(map(int,input().split()))
    for j in range(len(line)):
        if line[j]==1:
            graph[i].append(j+1)
for g in graph:
    print(len(graph[g]), *graph[g])
# print(graph)
