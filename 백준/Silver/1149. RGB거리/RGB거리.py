n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

min_cost = [[0]*3 for _ in range(n)]
min_cost[0][0], min_cost[0][1], min_cost[0][2] = cost[0][0], cost[0][1], cost[0][2]

for i in range(1, n):
    for j in range(3):
        min_cost[i][j] = cost[i][j] + \
            min(min_cost[i-1][j-1], min_cost[i-1][j-2])

print(min(min_cost[n-1]))