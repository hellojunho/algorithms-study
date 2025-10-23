from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)

com = set(combinations_with_replacement(nums, m))

for c in sorted(com):
    print(*c)