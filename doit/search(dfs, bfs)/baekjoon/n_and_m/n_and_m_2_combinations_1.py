import sys

from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

n_arr = [i for i in range(1, n+1)]


arr = list(combinations(n_arr, m))

for i in arr:
    print(i[0], end=" ")
    for j in range(1, m):
        print(i[j], end=" ")
    print()
