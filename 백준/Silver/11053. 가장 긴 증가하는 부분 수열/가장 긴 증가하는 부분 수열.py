n = int(input())
input_values = list(map(int, input().split(' ')))

max_values = [1] * n

for i in range(n):
    for j in range(i):
        if input_values[i] > input_values[j]:
            max_values[i] = max(max_values[j]+1, max_values[i])
        
print(max(max_values))
