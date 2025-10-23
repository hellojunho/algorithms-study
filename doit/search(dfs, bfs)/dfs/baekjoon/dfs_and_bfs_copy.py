import sys
from collections import deque


def dfs(v, visited):
    if v in visited:
        return
    visited.append(v)
    print(v, end=' ')
    for i in sorted(graph[v]):
        if i not in visited:
            dfs(i, visited)


def bfs(v, visited):
    q = deque([v])
    visited.append(v)

    while q:
        n = q.popleft()
        print(n, end=' ')
        for i in sorted(graph[n]):
            if i not in visited:
                visited.append(i)
                q.append(i)



input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(v, visited)
visited = []
print()
bfs(v, visited)