# import sys
# from itertools import combinations

# input = sys.stdin.readline

# while True:
#     nums = list(map(int, input().split()))
#     if nums[0] == 0:
#         break

#     com = set(combinations(nums[1:], 6))

#     for c in sorted(com):
#         print(*c)
#     print()


import sys

input = sys.stdin.readline


while True:
    nums = list(map(int, input().split()))
    k = nums[0]
    numbers = nums[1:]

    if k == 0:
        break

    result = []
    answer = []

    def combination(start):
        if len(result) == 6:
            answer.append(list(result))
            return
        
        for i in range(start, len(numbers)):
            result.append(numbers[i])
            combination(i+1)
            result.pop()

    combination(0)

    for combo in answer:
        print(*combo)
    print()