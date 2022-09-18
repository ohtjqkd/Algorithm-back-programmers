def solution(n, computers):
    answer = 0
    
    graph = dict()
    
    for i in range(len(computers)):
        graph[i] = [j for j in range(n) if computers[i][j] == 1]
    
    need_visit = list()
    visited = list()
    for i in range(n):
        if i not in visited:
            need_visit.append(i)
            answer += 1
        while need_visit:
            node = need_visit.pop()
            if node not in visited:
                visited.append(node)
                need_visit.extend(graph[node])
        # print(need_visit, visited)
        # print(graph)
    return answer