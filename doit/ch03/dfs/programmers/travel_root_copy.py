# airport = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

# # 모든 공항 코드로 딕셔너리 초기화
# airports = set()
# for a, b in airport:
#     airports.add(a)
#     airports.add(b)

# root = {airport_code: [] for airport_code in airports}

# for a, b in airport:
#     root[a].append(b)

# visited = {airport_code: False for airport_code in airports}

# def dfs(v, visited, root):
#     if visited[v] == True:
#         return
#     visited[v] = True
#     print(v, end=' ')
#     for r in root[v]:
#         if visited[r] == False:
#             dfs(r, visited, root)


def solution(tickets):
    answer = []
    visited = [False for _ in range(len(tickets) + 1)]
    path = []

    def dfs(start, path):
        print(path)
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return
        for i, t in enumerate(tickets):
            if t[0] == start and not visited[i]:
                visited[i] = True
                dfs(t[1], path + [t[1]]) # append()는 리스트를 수정한 후 None을 반환 (dfs(t[1], None)이 되므로 안됨)
                visited[i] = False
    dfs("ICN", ["ICN"])
    answer.sort()
    return answer[0]

if __name__ == "__main__":
    # tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    # print(solution(tickets))  # ["ICN", "JFK", "HND", "IAD"]
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    print(solution(tickets))  # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]