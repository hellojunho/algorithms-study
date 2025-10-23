def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    from collections import deque
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))

        return maps[len(maps) - 1][len(maps[0]) - 1]
    
    return -1 if bfs(0, 0) == 1 else bfs(0, 0)