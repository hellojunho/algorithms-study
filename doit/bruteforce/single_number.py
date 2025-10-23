import sys

input = sys.stdin.readline

n = int(input())
count = 0

for i in range(1, n+1):
    num = [int(i) for i in str(i)]
    if i < 100:
        count += 1
    elif num[0] - num[1] == num[1] - num[2]:
        count += 1

print(count)