from collections import deque
N = int(input())
deq = deque(range(1, N+1))
ret = []
while len(deq) > 1:
    ret.append(str(deq.popleft()))
    deq.append(deq.popleft())
ret.append(str(deq[0]))
print(' '.join(ret))