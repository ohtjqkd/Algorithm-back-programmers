from heapq import heappop, heappush

n, m = map(int, input().split())

h = []

nums = list(map(int, input().split()))

for i in range(n):
  heappush(h, nums[i])

for i in range(m):
  a = heappop(h)
  b = heappop(h)
  heappush(h, a+b)
  heappush(h, a+b)
  
print(sum(h))