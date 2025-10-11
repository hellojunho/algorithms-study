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
#         if remember != nums[i]:
#             result.append(nums[i])
#             remember = nums[i]
#             dfs(i)
#             result.pop()

# dfs(0)


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)

from itertools import combinations_with_replacement

comw = set(combinations_with_replacement(nums, m))

for c in sorted(comw):
    print(*c)