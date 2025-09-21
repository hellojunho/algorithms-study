# [문제 001] 숫자의 합
# https://www.acmicpc.net/problem/11720

import sys
input = sys.stdin.readline

n = input()
numbers = list(input().strip())

_sum = 0

for i in numbers:
    _sum += int(i)

print(_sum)