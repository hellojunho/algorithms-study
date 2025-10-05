import sys 

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

arr = [i for i in range(1, n+1)]
result = []

def dfs(node):
    if len(result) == m: # 중복제거
        print(*result)
        return
    
    for i in nums:
        if i in result:
            continue
        result.append(i)
        dfs(i)
        result.pop()

dfs(0)
