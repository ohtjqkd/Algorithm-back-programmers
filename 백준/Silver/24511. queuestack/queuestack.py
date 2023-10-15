from collections import deque

n = int(input())

t = list(map(int, input().split()))

v = list(map(int, input().split()))

m = int(input())

q = deque([])
for i in range(n - 1, -1, -1):
  if t[i] == 0:
    q.append(v[i])
    
inp = list(map(int, input().split()))

ret = []
for i in inp:
  q.append(i)
  ret.append(q.popleft())
print(' '.join(list(map(str, ret))))