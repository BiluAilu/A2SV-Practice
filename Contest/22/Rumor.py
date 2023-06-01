    
# def main():
#     n,p=map(int,input().split())
#     gold=list(map(int,input().split()))
#     pair=[]
#     for i in range(p):
#     pair.append(list(map(int,input().split())

#     result=0
#     if p==0:
#         for i in range(n):
#             result+=gold[i]
#         print(result)
#         return
#     else:



# main()


from collections import defaultdict
def main():
    visited=set()
    def dfs(start):
        stack=[start]
        while stack:
            node=stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)


    n,p=map(int,input().split())
    gold=list(map(int,input().split()))
    ans=0
    graph=defaultdict(list)
    for i in range(p):
        u,v=map(int,input().split()) 
        graph[u].append(v)
        graph[v].append(u)
    
    gold=sorted([(g,i+1) for i,g in enumerate(gold)])
    for g,i in gold:
        if i not in visited:
            ans+=g
            dfs(i)
    print(ans)
main()