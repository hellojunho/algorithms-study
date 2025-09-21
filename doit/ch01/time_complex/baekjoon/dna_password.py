import sys

input = sys.stdin.readline


n, m = map(int, input().split())
arr = input().strip()
a, c, g, t = map(int, input().split())

count = 0

start = 0
end = m


while end <= n:
    check = {"A": 0, "C": 0, "G": 0, "T": 0}
    dna = arr[start:end]
    for i in dna:
        check[i] += 1
    
    if check["A"] >= a and check["C"] >= c and check["G"] >= g and check["T"] >= t:
        count += 1
    start += 1
    end += 1

print(count)