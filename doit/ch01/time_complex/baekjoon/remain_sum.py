# 나머지 합 구하기
# https://www.acmicpc.net/problem/10986


n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0

for i in range(n):
    s = 0
    for j in range(i, n):
        s += arr[j]
        if s % m == 0:
            result += 1


print(result)