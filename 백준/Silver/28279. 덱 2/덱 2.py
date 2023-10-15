from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
d = deque([])
for i in range(n):
  cmd = list(map(int, input().split(' ')))
  match cmd[0]:
    case 1:
      d.appendleft(cmd[1])
    case 2:
      d.append(cmd[1])
    case 3:
      if len(d) == 0:
        print(-1)
      else:
        print(d.popleft())
    case 4:
      if len(d) == 0:
        print(-1)
      else:
        print(d.pop())
    case 5:
      print(len(d))
    case 6:
      if len(d) == 0:
        print(1)
      else:
        print(0)
    case 7:
      if len(d) == 0:
        print(-1)
      else:
        print(d[0])
    case 8:
      if len(d) == 0:
        print(-1)
      else:
        print(d[-1])
