def dfs(v, visited, graph):
    res = []

    if visited[v] == True:
        return
    
    visited[v] = True
    res.append(v)
    for g in graph[v]:
        if visited[g] == False:
            dfs(g, visited, graph)
    return res

def solution(tickets):
    answer = []
    airports = set()
    for a, b in tickets:
        airports.add(a)
        airports.add(b)
    
    graph = {airport: [] for airport in airports}
    for a, b in tickets:
        graph[a].append(b)
    
    visited = [False for _ in range(len(tickets) + 1)]
    for i in range(len(tickets) + 1):
        if not visited[i]:
            answer.append(dfs(i, visited, graph))

    print(answer)
    return 1


if __name__ == "__main__":
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    print(solution(tickets))  # ["ICN", "JFK", "HND", "IAD"]