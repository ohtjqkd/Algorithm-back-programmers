import sys, re

input = sys.stdin.readline

p = re.compile('(100+1+|01)+')
for i in range(int(input())):
  s = input().strip()
  if p.fullmatch(s):
    print('YES')
  else:
    print('NO')