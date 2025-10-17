import sys

input = sys.stdin.readline

def dfs(v, visited, graph):
    if visited[v]:
        return
    
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited, graph)


n, m = map(int, input().split())
count = 0
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)


for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, n+1):        
    if not visited[i]:
        dfs(i, visited, graph)
        count += 1

print(count)
