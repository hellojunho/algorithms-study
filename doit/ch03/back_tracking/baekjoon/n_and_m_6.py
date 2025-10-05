import sys 

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []

def dfs(node):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(node, n):
        if nums[i] in result:
            continue
        result.append(nums[i])
        dfs(i)
        result.pop()
    
dfs(0)
