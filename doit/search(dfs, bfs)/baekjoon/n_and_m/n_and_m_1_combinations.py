from itertools import combinations, permutations
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]


for c in list(permutations(arr, m)):
    print(*c)