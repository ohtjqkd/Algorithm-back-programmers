a, b = map(int, input().split())

ans = 1

while True:
  if a == b:
    print(ans)
    break
  elif a > b:
    print(-1)
    break
  elif b % 2 == 0:
    ans += 1
    b //= 2
  elif b % 10 == 1:
    ans += 1
    b //= 10
  else:
    print(-1)
    break
      