import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

result = []

def dfs(start):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(start, n+1):
        result.append(nums[i-1])
        dfs(i)
        result.pop()

dfs(1)