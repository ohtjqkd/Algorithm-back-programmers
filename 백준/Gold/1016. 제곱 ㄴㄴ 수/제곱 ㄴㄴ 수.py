import math


n, m = map(int, input().split())
prime = [1 for _ in range(int(m ** 0.5) + 1)]
prime[0], prime[1] = 0, 0
square = []
for i in range(2, len(prime)):
  if prime[i] == 1:
    for j in range(i + i, len(prime), i):
      prime[j] = 0
    square.append(i ** 2)

r = [1 for _ in range(m - n + 1)]

for i in square:
  start_num = math.ceil(n / i) * i
  for j in range(start_num, m + 1, i):
    r[j - n] = 0

print(sum(r))
