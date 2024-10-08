from functools import cmp_to_key

n, m = map(int, input().split())

arr = list(map(int, input().split()))

def compare(a: int, b: int):
  if a % 10 == 0 and b % 10 == 0:
    return a - b
  elif a % 10 == 0:
    return -1
  elif b % 10 == 0:
    return 1
  return a - b

arr.sort(key=cmp_to_key(compare))
ans = 0
for i in range(len(arr)):
  if m <= 0:
    break
  while arr[i] >= 10 and m > 0:
    arr[i] -= 10
    if arr[i] == 0:
      ans += 1
    elif arr[i] < 0:
      pass
    else:
      ans += 1
      m -= 1
    if m == 0 and arr[i] == 10:
      ans += 1

print(ans)