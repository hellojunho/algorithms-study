import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
k = int(input())
cards = []

for i in range(n):
    cards.append(int(input()))

per = permutations(cards, k)
re = set()
number = ''
for p in per:
    for i in range(k):
        number += str(p[i])
    re.add(number)
    number = ''

count = 0
for r in re:
    count += 1

print(count)