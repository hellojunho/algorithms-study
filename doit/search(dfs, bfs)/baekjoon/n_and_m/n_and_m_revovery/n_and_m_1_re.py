# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# result = []
# nums = [i for i in range(1, n+1)]
# visited = [False] * (n+1)

# def dfs(start):
#     if len(result) == m:
#         print(*result)
#         return
    
#     for i in range(1, n+1):
#         if visited[i] == False:
#             visited[i] = True
#             result.append(nums[i-1])
#             dfs(nums[i-1])
#             result.pop()
#             visited[i] = False


# dfs(0)


from itertools import permutations


n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

com = permutations(nums, m)

for c in com:
    print(*c)