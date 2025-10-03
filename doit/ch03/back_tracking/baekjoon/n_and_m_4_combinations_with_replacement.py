import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline
n, m = map(int, input().split())

combination = combinations_with_replacement(range(1, n+1), m)

for c in combination:
    print(*c)