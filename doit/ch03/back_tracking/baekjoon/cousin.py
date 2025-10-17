import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
result = []
visited = [False] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(v, count):
    if v == b:
        result.append(count)
    
    count += 1
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i, count)
        
dfs(a, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0])

# def dfs(a, vistied, graph):
#     if a == b:
#         return
#     visited[a] = True
#     for i in graph[a]:
#         if not visited[i]:
#             dfs(i, visited, graph)

# count = 0
# for i in range(n):
#     if not visited[i]:
#         dfs(i, visited, graph)
#         count += 1

# print(count)