from itertools import combinations

n, m = map(int, input().split())
n_arr = [i for i in range(1, n+1)]
arr = list(combinations(n_arr, m))

for i in arr:
    print(*i)
