import heapq

# n = 7
# input_values = [(1,6),(1,7),(3,2),(3,1),(2,4),(2,5),(6,1)]


heap_data = []
input_values = []

n = int(input())
for _ in range(n):
    dead, amount = map(int, input().split())
    input_values.append((dead,amount))

input_values.sort()

for dead, amount in input_values:
    
    heapq.heappush(heap_data, amount)
    if dead < len(heap_data):
        heapq.heappop(heap_data)
    
print(sum(heap_data))
