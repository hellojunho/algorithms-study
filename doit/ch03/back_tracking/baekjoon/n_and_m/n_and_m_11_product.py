from itertools import product

n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = []

com = list(product(sorted(nums), repeat=m))
com = sorted(list(set(com)))

for c in com:
    print(*c)