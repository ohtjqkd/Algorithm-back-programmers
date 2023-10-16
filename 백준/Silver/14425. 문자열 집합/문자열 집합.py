n, m = map(int, input().split())
answer = 0
S = set()

for _ in range(n):
  S.add(input())

for _ in range(m):
  if input() in S:
    answer += 1
print(answer)