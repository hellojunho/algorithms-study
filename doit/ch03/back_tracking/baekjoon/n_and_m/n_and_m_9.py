import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)
result = []

from itertools import combinations, permutations

cm = set(permutations(nums, m))

for c in sorted(cm):
    print(*c)
