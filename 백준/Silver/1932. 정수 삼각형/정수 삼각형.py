n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))
max_nodes = [[0]*(i+1) for i in range(n)]
max_nodes[0][0] = triangle[0][0]
for i in range(len(triangle)-1):
    for j in range(len(triangle[i])):
        max_nodes[i+1][j] = max(max_nodes[i][j]+triangle[i+1][j], max_nodes[i+1][j])
        max_nodes[i+1][j+1] = max(max_nodes[i][j]+triangle[i+1][j+1], max_nodes[i+1][j+1])
print(max(max_nodes[-1]))