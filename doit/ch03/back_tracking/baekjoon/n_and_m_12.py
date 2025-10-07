import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = []

def dfs(start):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(n+1):
        result.append(nums[i-1])
        dfs(nums[i-1])
        result.pop()

dfs(0)