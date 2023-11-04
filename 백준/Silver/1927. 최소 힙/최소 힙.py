import heapq, sys
input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    C = int(input())
    if C == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, C)