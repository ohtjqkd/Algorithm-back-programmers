import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))
result = 0
while len(heap) > 1:
    tmp1 = heapq.heappop(heap)
    tmp2 = heapq.heappop(heap)
    result = result + tmp1 + tmp2
    heapq.heappush(heap, tmp1+tmp2)

print(result)