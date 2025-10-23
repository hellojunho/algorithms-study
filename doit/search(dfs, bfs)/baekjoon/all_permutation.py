# import sys

# input = sys.stdin.readline

# n = int(input())
# nums = [i for i in range(1, n+1)]
# result = []
# visited = [False] * n

# def permutation(num):
#     if len(result) == n:
#         print(*result)
#         return
    
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = True
#             result.append(nums[i])
#             permutation(i)
#             visited[i] = False
#             result.pop()

# permutation(0)


import sys

input = sys.stdin.readline

n = int(input())
nums = [i for i in range(1, n+1)]


from itertools import permutations


per = permutations(nums, n)

for p in per:
    print(*p)