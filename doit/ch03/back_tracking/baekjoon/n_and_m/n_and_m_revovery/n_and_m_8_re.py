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
    
#     for i in range(start, n):
#             result.append(nums[i])
#             dfs(i)
#             result.pop()

# dfs(0)


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)

result = []


from itertools import combinations_with_replacement

com = combinations_with_replacement(nums, m)

for c in com:
    print(*c)