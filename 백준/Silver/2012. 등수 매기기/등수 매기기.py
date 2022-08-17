##problem 2012
n = int(input())
expected = []
occpied = [False] * n
for _ in range(n):
    expected.append(int(input()))


expected = sorted(expected)
result = 0
for i in range(len(expected)):
    difference = expected[i] - (i+1)
    if difference >= 0:
        result+=difference
    else:
        result-=difference

print(int(result))
    