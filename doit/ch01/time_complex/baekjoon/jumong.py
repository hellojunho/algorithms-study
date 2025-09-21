import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()

l, r = 0, n - 1
count = 0
while l < r:
    if arr[l] + arr[r] == m:
        count += 1
        l += 1
        r -= 1
    elif arr[l] + arr[r] < m:
        l += 1
    else:
        r -= 1

print(count)