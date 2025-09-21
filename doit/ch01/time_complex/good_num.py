import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

count = 0

for i in range(n):
    temp = arr[:i] + arr[i+1:]
    start, end = 0, len(temp) - 1

    while start < end:
        if temp[start] + temp[end] == arr[i]:
            count += 1
            break
        elif temp[start] + temp[end] < arr[i]:
            start += 1
        else:
            end -= 1

print(count)