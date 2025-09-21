# [문제 000] 수 정렬하기
# https://www.acmicpc.net/problem/2750

import sys

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

# nums.sort()

# for num in nums:
#     print(num)


# 버블 정렬
for i in range(n):
    for j in range(n-1-i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

for num in nums:
    print(num)