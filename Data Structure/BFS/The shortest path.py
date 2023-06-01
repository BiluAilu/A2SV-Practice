from collections import defaultdict,deque

n,m=map(int,input().split())
a,b=map(int,input().split())

graph=defaultdict(list)
for i in range(m):
    u,v=map(int,input().split())

    graph[u].append(v)
    graph[v].append(u)
visited=[False] * (n+1)
prev=[-1]*(n+1)
queue=deque((a,))


visited[a]=True

while queue:
    for _ in range(len(queue)):
        u=queue.popleft()
        if u==b:
            path=[]
            curr=u
            while curr!=-1:
                path.append(curr)
                curr=prev[curr]
            path.reverse()
            print(len(path)-1)
            print(*path)
            exit(0)
        for v in graph[u]:
            if visited[v]==False:
                prev[v]=u
                visited[v]=True
                queue.append(v)
        






