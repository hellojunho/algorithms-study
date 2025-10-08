# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# nums = [i for i in range(1, n+1)]
# result = []
# visited = [False] * (n+1)


# def dfs(start):
#     if len(result) == m:
#         print(*result)
#         return
    
#     for i in range(1, n+1):
#         result.append(i)
#         dfs(i)
#         result.pop()

# dfs(0)

from itertools import product

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

com = product(nums, repeat=m)

for c in com:
    print(*c)