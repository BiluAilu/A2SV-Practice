from collections import defaultdict
n,m=map(int,input().split())
graph=defaultdict(list)

for i in range(m):
    u,v=map(int,input().split())
    graph[v].apppend(u)
    graph[u].apppend(v)

if n>=m:
    print("no")
    exit()
else:
    

