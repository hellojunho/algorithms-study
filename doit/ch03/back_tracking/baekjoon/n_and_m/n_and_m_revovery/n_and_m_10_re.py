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
    
#     remember = 0
#     for i in range(start, n):
#         if not visited[i] and remember != nums[i]:
#             visited[i] = True
#             result.append(nums[i])
#             remember = nums[i]
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

com = set(combinations(nums, m))

for c in sorted(com):
    print(*c)