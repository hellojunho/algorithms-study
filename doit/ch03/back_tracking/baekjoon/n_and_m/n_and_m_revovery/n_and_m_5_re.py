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
#         if not visited[i]:
#             visited[i] = True
#             result.append(nums[i])
#             dfs(nums[i])
#             visited[i] = False
#             result.pop()

# dfs(0)


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)

result = []
visited = [False] * n


from itertools import permutations

per = permutations(nums, m)

for p in per:
    print(*p)