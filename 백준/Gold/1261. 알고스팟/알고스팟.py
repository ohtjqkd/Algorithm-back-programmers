import heapq
N, M = map(int, input().split())
maze = [list(input()) for _ in range(M)]
distances = [[float('inf') for _ in range(N)] for _ in range(M)]
heap = []
distances[0][0] = 0
heapq.heappush(heap, (0, 0, 0))
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
while heap:
    w, x, y = heapq.heappop(heap)
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if 0 <= xx < M and 0 <= yy < N:
            if maze[xx][yy] == '0' and distances[xx][yy] > w:
                heapq.heappush(heap, (w, xx, yy))
                distances[xx][yy] = w
            elif maze[xx][yy] == '1' and distances[xx][yy] > w+1:
                heapq.heappush(heap, (w+1, xx, yy))
                distances[xx][yy] = w+1
print(distances[-1][-1])