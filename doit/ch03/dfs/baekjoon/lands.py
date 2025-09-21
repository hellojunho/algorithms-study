import sys
sys.setrecursionlimit(10000)

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

def dfs(x, y, graph, visited):
    visited[x][y] = True
    for i in range(8):  # 대각선 포함
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny, graph, visited)


result = []
while True:
    w, h = map(int, input().split())  # 너비, 높이
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    count = 0
    if w == 0 and h == 0:
        break
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j, graph, visited)
                count += 1
    result.append(count)

for i in result:
    print(i)
