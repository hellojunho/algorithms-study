import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = set(map(int, input().split()))
result = []


def dfs(start):
    if len(result) == m:
        print(*result)
        return
    
    for i in sorted(nums):
        result.append(i)
        dfs(i)
        result.pop()

dfs(0)