# [문제 003] 구간 합 구하기 1
# https://www.acmicpc.net/problem/11659

n, m = map(int, input().split())
arr = list(map(int, input().split()))


# 구간 합 s (s[i] = arr[0] + ... + arr[i])
s = list()
temp = 0
s.append(0)
for i in arr:
    temp += i
    s.append(temp)


result = list()
for _ in range(m):
    i, j = map(int, input().split())

    # 범위 별 구간 합 s[j-1] - s[i]
    result.append(s[j] - s[i - 1])


for i in result:
    print(i)