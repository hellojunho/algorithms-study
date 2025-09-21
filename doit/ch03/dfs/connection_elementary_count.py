import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n + 1)] # 그래프 데이터 저장 인접 리스트는 왜 2차원배열?: 각 노드가 여러개의 간선을 가질 수 있기 때문에
visited = [False] * (n + 1) # 방문 기록 리스트

def DFS(v):
    visited[v] = True
    for i in a[v]:
        if not visited[i]:
            DFS(i)

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

count = 0

for i in range(1, n + 1):
    if not visited[i]:
        DFS(i)
        count += 1

print(count)