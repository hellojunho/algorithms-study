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
    
#     for i in range(n):
#         result.append(nums[i])
#         dfs(i)
#         result.pop()

# dfs(0)


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)

from itertools import product

com = product(nums, repeat=m)

for c in com:
    print(*c)