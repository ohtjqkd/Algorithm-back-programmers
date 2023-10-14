n = int(input())

def is_prime(num):
  if num == 0 or num == 1:
    return False
  for i in range(2, int(num**0.5)+1):
    if num % i == 0:
      return False
  return True

for i in range(n):
  s = int(input())
  while is_prime(s) == False:
    s += 1
  print(s)
