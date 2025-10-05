import sys

input = sys.stdin.readline

from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

permutation = combinations_with_replacement(nums, m)

for p in permutation:
    print(*p) 