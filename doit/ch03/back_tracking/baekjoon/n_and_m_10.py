n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []

from itertools import combinations

combination = set(combinations(nums, m))

for c in sorted(combination):
    print(*c)
