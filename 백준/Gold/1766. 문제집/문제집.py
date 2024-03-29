import heapq
n, m = map(int, input().split(' '))
array = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

heap = []
result = []


for _ in range(m):
    x, y = map(int, input().split(' '))
    array[x].append(y)
    indegree[y] += 1

for n in range(1, n+1):
    if indegree[n] == 0:
        heapq.heappush(heap, n)
        
while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(heap, y)

for r in result:
    print(r, end=' ')


