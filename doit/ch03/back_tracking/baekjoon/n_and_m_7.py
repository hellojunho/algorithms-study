# import sys 

# input = sys.stdin.readline

# n, m = map(int, input().split())
# nums = list(map(int, input().split()))
# nums.sort()
# result = []

# def dfs(node):
#     if len(result) == m:
#         print(*result)
#         return
    
#     for i in nums:
#         result.append(i)
#         dfs(i)
#         result.pop()
    
# dfs(0)


from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
for p in permutations(nums, m):
    print(*p)