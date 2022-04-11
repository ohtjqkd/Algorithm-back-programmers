from collections import deque

input_values = list()
n, m = map(int, input().split(' '))
for _ in range(m):
    a, b = map(int, input().split(' '))
    input_values.append((a,b))
max_virus = 0
result = []

edges = [[] for _ in range(n+1)]

for node, adjacent in input_values:
    edges[adjacent].append(node)
    
def bfs(node, visited):
    result = 0
    need_visit = deque()
    need_visit.append(node)
    visited[node] = True
    while need_visit:
        poped = need_visit.popleft()
        adjacents = edges[poped]
        for i in adjacents:
            if not visited[i]:
                need_visit.append(i)
                visited[i] = True
                result += 1
        
    return result

for i in range(1, n+1):
    visited = [False] * (n+1)
    out_put = bfs(i, visited)
    if max_virus < out_put:
        result = [i]
        max_virus = out_put
    elif max_virus == out_put:
        result.append(i)

for r in result:
    print(r, end=' ')
                
    
