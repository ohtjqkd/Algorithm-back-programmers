#트리

N = int(input())
parent = list(map(int, input().split(" ")))
T = int(input())
answer = 0

# 간선정보를 담기 위한 dictionary
edges = dict()

for i in range(len(parent)):
    if parent[i] == -1:
        root = i
    if i == T or parent[i] == T or parent[i] == -1:
        continue
    edges[parent[i]] = edges.get(parent[i], []) + [i]

# dfs를 통해 리프 노드를 탐색

# 루트 노드인 0으로 초기화
nodes = [root] 
if root == T:
    nodes.pop()

while nodes:
    curr_node = nodes.pop()
    nxt_nodes = edges.get(curr_node)
    if not nxt_nodes: # 다음 노드가 없으면 결과에 + 1
        answer += 1
    else:
        nodes.extend(nxt_nodes)
print(answer)