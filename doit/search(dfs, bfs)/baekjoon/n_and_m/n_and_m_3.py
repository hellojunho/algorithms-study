import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
result = []

# print(arr)

def DSF(node):
    print("result: ", result)
    if len(result) == m:
        print(*result)
        return
    
    for i in range(1, n+1):
        result.append(i)
        DSF(i + 1)
        result.pop()

DSF(1)
