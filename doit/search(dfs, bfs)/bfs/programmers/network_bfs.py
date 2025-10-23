def BFS(n, computers, com, visited):
    from collections import deque
    queue = deque([com])
    while queue:
        v = queue.popleft()
        visited[v] = True
        for c in range(n):
            if v != c and computers[v][c] == 1:
                if visited[c] == False:
                    queue.append(c)


def solution(n, computers):
    answer = 0
    visited = [ False for _ in range(n)]
    for com in range(n):
        if visited[com] == False:
            BFS(n, computers, com, visited)
            answer += 1
    return answer


if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, computers))  # 2
    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(solution(n, computers))  # 1