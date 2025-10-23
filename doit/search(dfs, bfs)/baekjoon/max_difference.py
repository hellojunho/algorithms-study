import sys


def get_diffenerence(nums, n):
    dif = 0
    for i in range(2, len(nums)+1):
        a = abs(nums[i-2] - nums[i-1])
        dif += a

    return dif


def permutation(start):
    if len(result) == n:
        ans.append(list(result))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result.append(nums[i])
            permutation(i)
            visited[i] = False
            result.pop()


input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

result = [] # 순열 과정 담는 리스트
visited = [False] * n # 방문 리스트
ans = [] # 순열 결과 리스트
answer = [] # 정답 출력

permutation(0)

for i in ans:
    answer.append(get_diffenerence(i, n))

print(max(answer))


# import sys
# from itertools import permutations


# def get_diffenerence(nums, n):
#     dif = 0
#     for i in range(2, len(nums)+1):
#         a = abs(nums[i-2] - nums[i-1])
#         dif += a

#     return dif

# input = sys.stdin.readline

# n = int(input())
# nums = list(map(int, input().split()))

# per = list(permutations(nums, n))
# result = []
# for i in per:
#     result.append(get_diffenerence(i, n))

# print(max(result))