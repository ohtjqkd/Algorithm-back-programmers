##testcode

# n, m, v = 4, 5, 1

# input_values = [[1,2], [1,3], [1,4], [2,4], [3,4]]

from collections import deque

graph = dict()
input_values = []

n, m, v = map(int, input().split(' '))
graph[v] = []
for _ in range(m):
    a, b = map(int, input().split(' '))
    input_values.append([a,b])



for x, y in input_values:
    graph[x] = []
    graph[y] = []

for node, adjacent in input_values:
    graph[node].append(adjacent)
    graph[adjacent].append(node)

    
def bfs(graph, start):
    need_visit = deque()
    visited = list()
    need_visit.append(start)
    
    while need_visit:
        poped_up = need_visit.popleft()

        if poped_up in visited:
            continue

        visited.append(poped_up)
        need_list = graph[poped_up]
        need_list.sort()
        for i in need_list:
            if i not in visited:
                need_visit.append(i)
                
    
    for i in visited:
        print(i, end=' ')
                

def dfs(graph, start):
    need_visit = deque()
    visited = list()
    need_visit.append(start)
    
    while need_visit:

        poped_up = need_visit.pop()
        if poped_up in visited:
            continue
            
        visited.append(poped_up)
        need_list = graph[poped_up]
        need_list.sort(reverse=True)
        for i in need_list:
            if i not in visited:
                need_visit.append(i)
                
    for i in visited:
        print(i, end=' ')
                
dfs(graph, v)
print()
bfs(graph, v)
