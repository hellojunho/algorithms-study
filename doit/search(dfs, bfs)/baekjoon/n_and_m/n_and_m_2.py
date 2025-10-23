import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
result = []

def DSF(node):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(node, n+1):
        result.append(i)
        DSF(i + 1)
        result.pop()

DSF(1)
