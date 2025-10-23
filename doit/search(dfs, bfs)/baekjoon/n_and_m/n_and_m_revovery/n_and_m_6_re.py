# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# nums = list(map(int, input().split()))
# nums = sorted(nums)

# result = []
# visited = [False] * n

# def dfs(start):
#     if len(result) == m:
#         print(*result)
#         return
    
#     for i in range(start, n): # 9 8 7 1 -> 1 7 8 9 -> 0: 1, 1: 7, 2: 8, 3: 9
#         if not visited[i]:
#             visited[i] = True
#             result.append(nums[i])
#             dfs(i)
#             visited[i] = False
#             result.pop()

# dfs(0)


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)

from itertools import combinations

com = combinations(nums, m)

for c in com:
    print(*c)