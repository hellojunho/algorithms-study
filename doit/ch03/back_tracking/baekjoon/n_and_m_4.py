# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = [i for i in range(1, n+1)]
# result = []

# def check_sort(arr):
#     val = arr[0]
#     for i in range(1, len(arr)):
#         if val > arr[i]:
#             return False
#         val = arr[i]
#     return True

# def DSF(node):
#     # print("DFS 시작", "node: ", node)
#     if len(result) == m:
#         if check_sort(result):
#             print(*result)
#         return
    
#     for i in range(1, n+1):
#         # print("i: ", i)
#         result.append(i)
#         # print("result: ", result)
#         DSF(i + 1)
#         result.pop()

# DSF(1)



import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
result = []

def check_sort(arr):
    val = arr[0]
    for i in range(1, len(arr)):
        if val > arr[i]:
            return False
        val = arr[i]
    return True

def DSF(node):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(node, n+1):
        result.append(i)
        DSF(i)
        result.pop()

DSF(1)
