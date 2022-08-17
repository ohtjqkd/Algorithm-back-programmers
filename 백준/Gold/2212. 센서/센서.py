n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()
distances = [sensors[i+1]-sensors[i] for i in range(len(sensors)-1)]


distances.sort()
result = 0
for i in range(n-k):
    result+=distances[i]

print(result)