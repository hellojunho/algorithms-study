import sys

input = sys.stdin.readline

count = 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n):
    s = 0
    for j in range(i, n):
        s += arr[j]
        if s == m:
            count += 1
            break
        elif s > m:
            break

print(count)

# l, r = 0, 0

# while (r<n):
#     s = sum(arr[l:r+1])
#     if s == m:
#         count += 1
#         l += 1
#     elif s > m:
#         l += 1
#     else:
#         r += 1