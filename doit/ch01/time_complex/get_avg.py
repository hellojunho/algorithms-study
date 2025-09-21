# [문제 002] 평균 구하기
# https://www.acmicpc.net/problem/1546

n = int(input())

arr = list(map(int, input().split()))

m = max(arr)

for i in range(n):
    arr[i] = arr[i] / m * 100

print(sum(arr) / n)