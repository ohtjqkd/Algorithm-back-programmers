import sys
input = sys.stdin.readline
n = int(input())
s = []
for i in range(n):
  cmd = list(map(int, input().split(' ')))
  c = cmd[0]
  match c:
    case 1:
      s.append(cmd[1])
    case 2:
      if len(s) > 0:
        print(s.pop())
      else:
        print(-1)
    case 3:
      print(len(s))
    case 4:
      if len(s) > 0:
        print(0)
      else:
        print(1)
    case 5:
      if len(s) > 0:
        print(s[-1])
      else:
        print(-1)
