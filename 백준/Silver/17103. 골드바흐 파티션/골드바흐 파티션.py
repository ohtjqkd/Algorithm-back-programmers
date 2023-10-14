is_prime = [1 for _ in range(1000001)]
is_prime[0], is_prime[1] = 0, 0
prime = []
prime_set = set()
for i in range(2, 1000001):
  if is_prime[i] == 1:
    prime.append(i)
    prime_set.add(i)
    mul = 1
    while i * mul <= 1000000:
      is_prime[i * mul] = 0
      mul += 1

gold_cnt = [0 for _ in range(1000001)]

T = int(input())

for i in range(T):
  n = int(input())
  cnt = 0
  for p in prime:
    if prime_set.__contains__(n - p) and p <= n - p:
      cnt += 1
  print(cnt)