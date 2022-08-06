import math

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(one, two):
    parent[find(two)] = find(one)
        
def get_distance(a, b):
    h = a[0]-b[0]
    v = a[1]-b[1]
    return math.sqrt(h**2+v**2)


n, m = map(int, input().split())

distance = [[float('inf')] * (n+1) for _ in range(n+1)]
parent = [i for i in range(n+1)]
edges = []
location = []
result = 0


for _ in range(n):
    x, y = map(int, input().split())
    location.append((x,y))
for i in range(n):
    for j in range(i+1, n):
        edges.append((i+1,j+1, get_distance(location[i], location[j])))

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)
        
edges = sorted(edges, key=lambda x: x[2])
for node1, node2, cost in edges:
    if find(node1) != find(node2):
        union(node1, node2)
        result+=cost
print("%0.2f" % result)