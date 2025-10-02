

begin = "hit"
target = "cog"
words = ["hit", "cog", "hot", "dot", "dog", "lot", "log"]


from collections import deque

def bfs(begin, target, words):
    q = deque()
    q.append([begin, 0])
    
    while q:
        current, step = q.popleft()

        if current == target:
            return step

        for w in words:
            count = 0
            for i in range(len(w)):
                if current[i] != w[i]:
                    count += 1
            if count == 1:
                q.append([w, step + 1])


def solution(begin, target, words):
    if target not in words:
        return 0
    return bfs(begin, target, words)


if __name__ == "__main__":
    print(solution(begin, target, words))  # 4