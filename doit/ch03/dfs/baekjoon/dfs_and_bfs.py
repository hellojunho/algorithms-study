import sys
from collections import deque
# sys.setrecursionlimit(10000)

def dfs(v, visited):
    if v in visited:
        return
    visited.append(v)
    print(v, end=' ')
    for i in sorted(graph[v]):
        if i not in visited:
            dfs(i, visited)


def bfs(v, visited):
    queue = deque([v])
    visited.append(v)
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if i not in visited:
                visited.append(i)
                queue.append(i)


input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = []

# 인접리스트 만들기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(v, visited)
visited = []
print()
bfs(v, visited)