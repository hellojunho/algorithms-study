import sys
sys.setrecursionlimit(10**6)


input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    p = [0] + nums
    visited = [False] * (n + 1)
    count = 0

    def dfs(v):
        visited[v] = True
        nxt = p[v]
        if not visited[nxt]:
            dfs(nxt)

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            count += 1

    print(count)



# def dfs(v):
#     visited[v] = True
#     number = numbers[v]
#     if not visited[number]:
#         dfs(number)


# for _ in range(int(input())):
#     n = int(input())
#     numbers = [0] + list(map(int, input().split()))
#     visited = [True] + [False] * n
#     count = 0

#     for i in range(1, n+1):
#         if not visited[i]:
#             dfs(i)
#             count += 1

#     print(count)