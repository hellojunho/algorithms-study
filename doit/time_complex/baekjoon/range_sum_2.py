# [문제 003] 구간 합 구하기 2
# https://www.acmicpc.net/problem/11660

n, m = map(int, input().split())
nums = []

for i in range(n):
    nums.append(list(map(int, input().split())))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + nums[i - 1][j - 1]

    
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(result)


# def solution(n, m, arr, x1, y1, x2, y2):
#     s = [[0] * (n) for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             s[i][j] = arr[i][j]
#             if i > 0:
#                 s[i][j] += s[i - 1][j]
#             if j > 0:
#                 s[i][j] += s[i][j - 1]
#             if i > 0 and j > 0:
#                 s[i][j] -= s[i - 1][j - 1]

#     return s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1]


# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]

# # 2차원 배열 구간 합 s s[i][j] = s[i][j-1] + s[i-1][j] - s[i-1][j-1] + arr[i][j]
# s = [[0] * (n) for _ in range(n)]

# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())

#     print(solution(n, m, arr, x1-1, y1-1, x2-1, y2-1))