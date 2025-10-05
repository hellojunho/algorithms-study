import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

for p in permutations(nums, m):
    print(*p)
