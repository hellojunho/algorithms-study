import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
visited = [False] * (n+1)
result = []

print(arr)

def DSF(node):
    print("visited: ", visited)
    print("result: ", result)
    if len(result) == m:
        print(*result)
        return
    
    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            DSF(i + 1)
            visited[i] = False
            # print("pop: ", result.pop())
            result.pop()

DSF(1)
