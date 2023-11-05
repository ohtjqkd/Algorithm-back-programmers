import sys

input = sys.stdin.readline
N = int(input())
ret = 0
for _ in range(N):
    ret += (int(input())-1)
print(ret+1)