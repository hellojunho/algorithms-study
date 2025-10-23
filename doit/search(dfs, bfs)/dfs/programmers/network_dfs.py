def DFS(n, computers, com, visited):
    if visited[com] == True:
        return
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            DFS(n, computers, connect, visited)


def solution(n, computers):
    answer = 0
    visited = [ False for _ in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1
    return answer


if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, computers))  # 2
    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(solution(n, computers))  # 1