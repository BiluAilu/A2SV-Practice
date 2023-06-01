import sys
from collections import defaultdict
n=int(input())

input = sys.stdin.readline
k = int(input().strip())
graph=defaultdict(list)
for i in range(k):
    line=list(map(int,input().split()))
    typ=line[0]
    if typ==1:
        graph[line[1]].append(line[2])
        graph[line[2]].append(line[1])
        
    
    else:
        print(*graph[line[1]])



