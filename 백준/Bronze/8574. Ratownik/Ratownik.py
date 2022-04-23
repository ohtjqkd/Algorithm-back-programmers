inputs = input().split(" ")
n, k, x, y = int(inputs[0]), int(inputs[1]), int(inputs[2]), int(inputs[3])
result = 0
for _ in range(n):
    line = input().split(" ")
    xi, yi = int(line[0]), int(line[1])
    if (x - xi) ** 2 + (y - yi) ** 2 > k ** 2:
        result += 1
print(result)