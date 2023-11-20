import heapq
N = int(input())
X, Y = map(int, input().split(" "))
M = int(input())
fam = {}
for _ in range(M):
    x, y = map(int, input().split(" "))
    fam[x] = fam.get(x, []) + [y]
    fam[y] = fam.get(y, []) + [x]
distances = [float('inf') for _ in range(N+1)]
heap = []
heapq.heappush(heap, (0, X))
distances[X] = 0
while heap:
    w, node = heapq.heappop(heap)
    for n in fam.get(node, []):
        if distances[n] > w+1:
            heapq.heappush(heap, (w+1, n))
            distances[n] = w+1
print(distances[Y] if distances[Y] != float('inf') else -1)