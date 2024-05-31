# 트리의 부모 찾기

# 주어지는 간선 정보에서 방향성을 알 수 없기 때문에 일단 후보로 넣어둠
import sys

input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N+1)]
parent = [0] * (N + 1)
visited = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split(" "))
    edges[a].append(b)
    edges[b].append(a)
nodes = [1]
while nodes:
    curr = nodes.pop()
    visited[curr] = 1
    children = edges[curr]
    for child in children:
        if visited[child] == 1:
            continue
        parent[child] = curr
        nodes.append(child)

for i in range(2, N + 1):
    print(parent[i])