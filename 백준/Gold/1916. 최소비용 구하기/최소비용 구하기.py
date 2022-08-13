from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
M = int(input())
maps = [{} for _ in range(N+1)]
fee = [INF for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split(" "))
    maps[s][e] = min(maps[s].get(e, INF), w)
start, end = map(int, input().split(" "))
heap = []
fee[start] = 0
heappush(heap, (fee[start], start))
while heap:
    w, s = heappop(heap)
    if fee[s] < w:
        continue
    nxt = maps[s].items()
    for n, nw in nxt:
        if fee[n] > w+nw:
            fee[n] = w+nw
            heappush(heap, (w+nw, n))
print(fee[end])