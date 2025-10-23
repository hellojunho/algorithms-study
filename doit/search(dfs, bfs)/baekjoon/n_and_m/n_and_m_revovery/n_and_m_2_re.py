import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
result = []
visited = [False] * (n+1)

def dfs(start):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(start, n+1):
        if visited[i] == False:
            if nums[i-1] in result:
                continue
            visited[i] = True
            result.append(nums[i-1])
            dfs(nums[i-1])
            visited[i] = False
            result.pop()

dfs(1)
            