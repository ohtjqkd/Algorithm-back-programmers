# 회사 문화1

import sys

input = sys.stdin.readline

n, m = map(int, input().split(" "))
boss = list(map(int, input().split(" ")))
score = [0] * n
edges = [[] for _ in range(n + 1)]
for i, b in enumerate(boss):
    if b == -1:
        continue
    edges[b - 1].append(i)

for _ in range(m):
    e, w = map(int, input().split(" "))
    score[e-1] += w
nodes = [0]
while nodes:
    curr = nodes.pop()
    children = edges[curr]
    for c in children:
        score[c] += score[curr]
        nodes.append(c)
print(' '.join(map(str, score)))