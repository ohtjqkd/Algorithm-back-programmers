from collections import defaultdict, deque
n = int(input())
idx_map = defaultdict(deque)
A = list(map(int, input().split()))
B = sorted(A)
for idx, a in enumerate(B):
  idx_map[a].append(idx)
ret = [str(idx_map[a].popleft()) for a in A]
print(' '.join(ret))